from auth_app import AuthApp
from controllers.user import user_bp
from controllers.auth import auth_bp


def init_app(app: AuthApp):
    # 登录认证蓝图
    app.register_blueprint(auth_bp)
    # 注册用户管理蓝图
    app.register_blueprint(user_bp)
    return None
