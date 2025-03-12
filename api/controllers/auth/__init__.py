# 登录管理
from flask import Blueprint

from .login_auth import LoginApi, LogoutApi, RefreshTokenApi, GetLoginProfile
from libs.external_api import ExternalApi

auth_bp = Blueprint('LoginAuth', __name__, url_prefix='/api/auth')
api = ExternalApi(auth_bp)

api.add_resource(LoginApi, '/login')
api.add_resource(LogoutApi, '/logout')
api.add_resource(RefreshTokenApi, '/refresh-token')
api.add_resource(GetLoginProfile, '/profile')
