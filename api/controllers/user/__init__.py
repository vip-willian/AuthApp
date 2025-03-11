# 用户管理
from flask import Blueprint

from .user import GetUserList, GetUserById, UserRegister
from .login import LoginApi, LogoutApi, RefreshTokenApi
from libs.external_api import ExternalApi

user_bp = Blueprint('user', __name__, url_prefix='/user/api')
api = ExternalApi(user_bp)

# 注册用户API
api.add_resource(GetUserById, '/get/<int:id>')
api.add_resource(GetUserList, '/list')
api.add_resource(UserRegister, '/register')

api.add_resource(LoginApi, '/login')
api.add_resource(LogoutApi, '/logout')
api.add_resource(RefreshTokenApi, '/refresh-token')
