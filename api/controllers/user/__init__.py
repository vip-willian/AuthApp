# 用户管理
from flask import Blueprint

from .user import GetUserList, UserLogin, UserLogout, GetUserById
from api.libs.external_api import ExternalApi

user_bp = Blueprint('user', __name__, url_prefix='/user/api')
api = ExternalApi(user_bp)

# 注册用户API
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(GetUserById, '/get/<int:id>')
api.add_resource(GetUserList, '/list')