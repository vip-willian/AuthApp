from api.auth_app import AuthApp
from api.controllers.user import user_bp


def init_app(app: AuthApp):
    # 注册用户管理蓝图
    app.register_blueprint(user_bp)
    return None
