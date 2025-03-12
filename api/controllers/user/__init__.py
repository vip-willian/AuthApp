# 用户管理
from flask import Blueprint

from .user import GetUserList, GetUserById, UserRegister
from libs.external_api import ExternalApi

user_bp = Blueprint('user', __name__, url_prefix='/api/user')
api = ExternalApi(user_bp)

# 注册用户API
api.add_resource(GetUserById, '/get/<int:id>')
api.add_resource(GetUserList, '/list')
api.add_resource(UserRegister, '/register')
