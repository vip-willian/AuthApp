import flask_login
from flask_restful import Resource, reqparse, request, marshal_with, marshal

from libs.password import valid_password
from services.login_auth_service import LoginAuthService
from services.errors.account import *
from libs.helper import extract_remote_ip
from typing import cast
from models.user import User
from controllers.error import UserBannedError, UserNameOrPasswordMismatchError, UserNotFound
from fields.login_field import current_user_detail_fields, success_field
from flask_login import login_required


class LoginApi(Resource):

    def post(self):
        # 解析登录的参数
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True, location="json")
        parser.add_argument("password", type=valid_password, required=True, location="json")
        parser.add_argument("remember_me", type=bool, required=False, location="json")

        args = parser.parse_args()

        try:
            # 校验账号信息在数据库中是否存在，以及用户名密码是否匹配
            user = LoginAuthService.authenticate(args["username"], args["password"])
        except UserLoginError:
            raise UserBannedError()
        except UserPasswordError:
            raise UserNameOrPasswordMismatchError()
        except UserNotFoundError:
            raise UserNotFound()
        # 执行登录，生成访问Token
        token_pair = LoginAuthService.login(user=user, ip_address=extract_remote_ip(request))
        return {"code": 200, "message": "ok", "data": token_pair.model_dump()}


class LogoutApi(Resource):

    def get(self):
        user = cast(User, flask_login.current_user)
        if isinstance(user, flask_login.AnonymousUserMixin):
            return {"result": "success"}
        LoginAuthService.logout(user=user)
        flask_login.logout_user()
        return {"result": "success"}


class RefreshTokenApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("refresh_token", type=str, required=True, location="json")
        args = parser.parse_args()

        try:
            new_token_pair = LoginAuthService.refresh_token(args["refresh_token"])
            return {"result": "success", "data": new_token_pair.model_dump()}
        except Exception as e:
            return {"result": "fail", "data": str(e)}, 401


class GetLoginProfile(Resource):

    @login_required
    def get(self):
        user = cast(User, flask_login.current_user)
        return {"code": 200, "message": "ok", "data": marshal(user, current_user_detail_fields)}
