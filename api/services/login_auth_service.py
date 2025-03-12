import base64
import secrets

from pydantic import BaseModel
from typing import cast, Optional
from datetime import UTC, datetime, timedelta
from configs import auth_config
from libs.passport import PassportService
from models.user import User, UserStatus
from models import db
from .errors.account import UserNotFoundError, UserLoginError, UserPasswordError
from libs.password import hash_password, compare_password
from extensions.ext_redis import redis_client
from werkzeug.exceptions import Unauthorized


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str


REFRESH_TOKEN_PREFIX = "refresh_token:"
LOGIN_REFRESH_TOKEN_PREFIX = "login_refresh_token:"
REFRESH_TOKEN_EXPIRE = timedelta(days=auth_config.REFRESH_TOKEN_EXPIRE_DAYS)

class LoginAuthService:

    @staticmethod
    def load_in_account(*, user_id: str):
        return LoginAuthService.load_user(user_id=int(user_id))

    @staticmethod
    def authenticate(username: str, password: str) -> User:
        # 根据用户名查询唯一个用户账号信息
        user = db.session.query(User).filter_by(username=username).first()
        if not user:
            raise UserNotFoundError

        if user.user_status == UserStatus.BANNED.value:
            raise UserLoginError("Account is banned.")

        if password and user.password is None:
            # 获取加盐字符串
            salt = secrets.token_bytes(16)
            # 将加盐字符串进行base64编码
            base64_salt = base64.b64encode(salt).decode()
            # 将密码进行加盐之后hash
            password_hashed = hash_password(password, salt)
            # 将hash之后的密码进行bas4编码
            base64_password_hashed = base64.b64encode(password_hashed).decode()
            user.password = base64_password_hashed
            user.password_salt = base64_salt

        if user.password is None or not compare_password(password, user.password, user.password_salt):
            raise UserPasswordError("Invalid username or password.")

        if user.user_status == UserStatus.PENDING.value:
            user.user_status = UserStatus.ACTIVE.value
            user.initialized_at = datetime.now(UTC).replace(tzinfo=None)

        db.session.commit()

        return cast(User, user)

    @staticmethod
    def login(user: User, *, ip_address: Optional[str] = None) -> TokenPair:

        if ip_address:
            LoginAuthService.update_login_info(user, ip_address=ip_address)

        if user.user_status == UserStatus.PENDING.value:
            user.user_status = UserStatus.ACTIVE.value
            db.session.commit()

        # 获取访问token
        access_token = LoginAuthService.get_account_jwt_token(user)
        # 生成刷新token
        refresh_token = _generate_refresh_token()

        # 存储更新Token
        LoginAuthService._store_refresh_token(refresh_token, user.id)

        return TokenPair(access_token=access_token, refresh_token=refresh_token)

    @staticmethod
    def update_login_info(user: User, *, ip_address: str) -> None:

        user.last_login_at = datetime.now(UTC).replace(tzinfo=None)
        user.last_login_ip = ip_address
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_account_jwt_token(user: User) -> str:

        # 过期时间
        exp_dt = datetime.now(UTC) + timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        exp = int(exp_dt.timestamp())

        payload = {
            "user_id": user.id,
            "exp": exp,
            "iss": auth_config.EDITION,
            "sub": "Auth API Passport"
        }

        token = PassportService().issue(payload)
        return token

    @staticmethod
    def logout(*, user: User) -> None:
        refresh_token = redis_client.get(LoginAuthService._get_account_refresh_token_key(user.id))
        if refresh_token:
            LoginAuthService._delete_refresh_token(refresh_token.decode("utf-8"), user.id)

    @staticmethod
    def _get_refresh_token_key(refresh_token):
        return f"{REFRESH_TOKEN_PREFIX}{refresh_token}"

    @staticmethod
    def _get_account_refresh_token_key(user_id):
        return f"{LOGIN_REFRESH_TOKEN_PREFIX}{user_id}"

    @staticmethod
    def _store_refresh_token(refresh_token: str, user_id: int) -> None:
        redis_client.setex(LoginAuthService._get_refresh_token_key(refresh_token), REFRESH_TOKEN_EXPIRE, user_id)
        redis_client.setex(LoginAuthService._get_account_refresh_token_key(user_id), REFRESH_TOKEN_EXPIRE,
                           refresh_token)

    @staticmethod
    def _delete_refresh_token(refresh_token: str, user_id: int) -> None:
        redis_client.delete(LoginAuthService._get_refresh_token_key(refresh_token))
        redis_client.delete(LoginAuthService._get_account_refresh_token_key(user_id))

    @staticmethod
    def refresh_token(refresh_token: str) -> TokenPair:

        user_id = redis_client.get(LoginAuthService._get_refresh_token_key(refresh_token))
        if not user_id:
            raise ValueError("Invalid refresh token")
        user = LoginAuthService.load_user(user_id.decode("utf-8"))
        if not user:
            raise ValueError("Invalid account")

        new_access_token = LoginAuthService.get_account_jwt_token(user)
        new_refresh_token = _generate_refresh_token()

        LoginAuthService._delete_refresh_token(refresh_token, user.id)
        LoginAuthService._store_refresh_token(new_refresh_token, user.id)

        return TokenPair(access_token=new_access_token, refresh_token=new_refresh_token)

    @staticmethod
    def load_user(user_id: int) -> None | User:
        user = db.session.query(User).filter_by(id=user_id).first()
        if not user:
            return None
        if user.user_status == UserStatus.BANNED.value:
            raise Unauthorized("Account is banned.")

        if datetime.now(UTC).replace(tzinfo=None) - user.last_active_at > timedelta(minutes=10):
            user.last_active_at = datetime.now(UTC).replace(tzinfo=None)
            db.session.commit()

        return cast(User, user)


def _generate_refresh_token(length: int = 64):
    token = secrets.token_hex(length)
    return token
