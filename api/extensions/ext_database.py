from auth_app import AuthApp
from models import db


def init_app(app: AuthApp):
    db.init_app(app)
