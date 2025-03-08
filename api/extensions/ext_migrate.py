from api.auth_app import AuthApp


def init_app(app: AuthApp):
    import flask_migrate
    from api.extensions.ext_database import db

    # 绑定数据库和迁移程序
    flask_migrate.Migrate(app, db)
