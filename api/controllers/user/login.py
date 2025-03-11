import flask_login
from flask_restful import Resource, reqparse, request, marshal_with
from libs.field_validate import email
from libs.password import valid_password
from services.account_service import AccountService
from services.errors.account import *
from libs.helper import extract_remote_ip
from typing import cast
from models.account import Account
from controllers.error import AccountBannedError, EmailOrPasswordMismatchError, AccountNotFound
from fields.login_field import current_user_detail_fields


class LoginApi(Resource):

    def post(self):
        # 解析登录的参数
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=email, required=True, location="json")
        parser.add_argument("password", type=valid_password, required=True, location="json")
        # parser.add_argument("remember_me", type=bool, required=False, location="json")

        args = parser.parse_args()

        try:
            # 校验账号信息在数据库中是否存在，以及邮箱密码是否匹配
            account = AccountService.authenticate(args["email"], args["password"])
        except AccountLoginError:
            raise AccountBannedError()
        except AccountPasswordError:
            raise EmailOrPasswordMismatchError()
        except AccountNotFoundError:
            raise AccountNotFound()
        # 执行登录，生成访问Token
        token_pair = AccountService.login(account=account, ip_address=extract_remote_ip(request))
        return {"status": 200, "result": "success", "data": token_pair.model_dump()}


class LogoutApi(Resource):

    def get(self):
        account = cast(Account, flask_login.current_user)
        if isinstance(account, flask_login.AnonymousUserMixin):
            return {"result": "success"}
        AccountService.logout(account=account)
        flask_login.logout_user()
        return {"result": "success"}


class RefreshTokenApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("refresh_token", type=str, required=True, location="json")
        args = parser.parse_args()

        try:
            new_token_pair = AccountService.refresh_token(args["refresh_token"])
            return {"result": "success", "data": new_token_pair.model_dump()}
        except Exception as e:
            return {"result": "fail", "data": str(e)}, 401


class GetCurrentLoginUser(Resource):
    @marshal_with(current_user_detail_fields)
    def get(self):
        account = cast(Account, flask_login.current_user)
        return account
