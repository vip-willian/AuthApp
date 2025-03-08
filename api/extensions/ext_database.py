from api.auth_app import AuthApp
from api.models import db


def init_app(app: AuthApp):
    db.init_app(app)
