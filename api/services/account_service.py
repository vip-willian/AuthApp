import base64
import secrets

from pydantic import BaseModel
from typing import cast, Optional
from datetime import UTC, datetime, timedelta
from api.configs import auth_config
from api.libs.passport import PassportService
from api.models.account import Account, AccountStatus
from api.models import db
from .errors.account import AccountNotFoundError, AccountLoginError, AccountPasswordError
from api.libs.password import hash_password, compare_password
from api.extensions.ext_redis import redis_client
from werkzeug.exceptions import Unauthorized


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str


REFRESH_TOKEN_PREFIX = "refresh_token:"
ACCOUNT_REFRESH_TOKEN_PREFIX = "account_refresh_token:"
REFRESH_TOKEN_EXPIRE = timedelta(days=auth_config.REFRESH_TOKEN_EXPIRE_DAYS)


class AccountService:

    @staticmethod
    def load_in_account(*, account_id: str):
        return AccountService.load_user(user_id=account_id)

    @staticmethod
    def authenticate(email: str, password: str) -> Account:
        # 根据email查询唯一个用户账号信息
        account = db.session.query(Account).filter_by(email=email).first()
        if not account:
            raise AccountNotFoundError

        if account.status == AccountStatus.BANNED.value:
            raise AccountLoginError("Account is banned.")

        if password and account.password is None:
            # 获取加盐字符串
            salt = secrets.token_bytes(16)
            # 将加盐字符串进行base64编码
            base64_salt = base64.b64encode(salt).decode()
            # 将密码进行加盐之后hash
            password_hashed = hash_password(password, salt)
            # 将hash之后的密码进行bas4编码
            base64_password_hashed = base64.b64encode(password_hashed).decode()
            account.password = base64_password_hashed
            account.password_salt = base64_salt

        if account.password is None or not compare_password(password, account.password, account.password_salt):
            raise AccountPasswordError("Invalid email or password.")

        if account.status == AccountStatus.PENDING.value:
            account.status = AccountStatus.ACTIVE.value
            account.initialized_at = datetime.now(UTC).replace(tzinfo=None)

        db.session.commit()

        return cast(Account, account)

    @staticmethod
    def login(account: Account, *, ip_address: Optional[str] = None) -> TokenPair:

        if ip_address:
            AccountService.update_login_info(account, ip_address=ip_address)

        if account.status == AccountStatus.PENDING.value:
            account.status = AccountStatus.ACTIVE.value
            db.session.commit()

        # 获取访问token
        access_token = AccountService.get_account_jwt_token(account=account)
        # 生成刷新token
        refresh_token = _generate_refresh_token()

        # 存储更新Token
        AccountService._store_refresh_token(refresh_token, account.id)

        return TokenPair(access_token=access_token, refresh_token=refresh_token)

    @staticmethod
    def update_login_info(account: Account, *, ip_address: str) -> None:

        account.last_login_at = datetime.now(UTC).replace(tzinfo=None)
        account.last_login_ip = ip_address
        db.session.add(account)
        db.session.commit()

    @staticmethod
    def get_account_jwt_token(account: Account) -> str:

        # 过期时间
        exp_dt = datetime.now(UTC) + timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        exp = int(exp_dt.timestamp())

        payload = {
            "user_id": account.id,
            "exp": exp,
            "iss": auth_config.EDITION,
            "sub": "Console API Passport"
        }

        token = PassportService().issue(payload)
        return token

    @staticmethod
    def logout(*, account: Account) -> None:
        refresh_token = redis_client.get(AccountService._get_account_refresh_token_key(account.id))
        if refresh_token:
            AccountService._delete_refresh_token(refresh_token.decode("utf-8"), account.id)

    @staticmethod
    def _get_refresh_token_key(refresh_token):
        return f"{REFRESH_TOKEN_PREFIX}{refresh_token}"

    @staticmethod
    def _get_account_refresh_token_key(account_id):
        return f"{ACCOUNT_REFRESH_TOKEN_PREFIX}{account_id}"

    @staticmethod
    def _store_refresh_token(refresh_token: str, account_id: str) -> None:
        redis_client.setex(AccountService._get_refresh_token_key(refresh_token), REFRESH_TOKEN_EXPIRE, account_id)
        redis_client.setex(AccountService._get_account_refresh_token_key(account_id), REFRESH_TOKEN_EXPIRE,
                           refresh_token)

    @staticmethod
    def _delete_refresh_token(refresh_token: str, account_id: str) -> None:
        redis_client.delete(AccountService._get_refresh_token_key(refresh_token))
        redis_client.delete(AccountService._get_account_refresh_token_key(account_id))

    @staticmethod
    def refresh_token(refresh_token: str) -> TokenPair:

        account_id = account_id = redis_client.get(AccountService._get_refresh_token_key(refresh_token))
        if not account_id:
            raise ValueError("Invalid refresh token")
        account = AccountService.load_user(account_id.decode("utf-8"))
        if not account:
            raise ValueError("Invalid account")

        new_access_token = AccountService.get_account_jwt_token(account=account)
        new_refresh_token = _generate_refresh_token()

        AccountService._delete_refresh_token(refresh_token, account.id)
        AccountService._store_refresh_token(new_refresh_token, account.id)

        return TokenPair(access_token=new_access_token, refresh_token=new_refresh_token)

    @staticmethod
    def load_user(user_id: str) -> None | Account:
        account = db.session.query(Account).filter_by(id=user_id).first()
        if not account:
            return None
        if account.status == AccountStatus.BANNED.value:
            raise Unauthorized("Account is banned.")

        if datetime.now(UTC).replace(tzinfo=None) - account.last_active_at > timedelta(minutes=10):
            account.last_active_at = datetime.now(UTC).replace(tzinfo=None)
            db.session.commit()

        return cast(Account, account)


def _generate_refresh_token(length: int = 64):
    token = secrets.token_hex(length)
    return token
