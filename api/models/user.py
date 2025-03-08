from api.models import db


class Syuser(db.Model):
    __tablename__ = 'sysuser'
    ID = db.Column(db.String(36), primary_key=True)
    AGE = db.Column(db.Integer)
    CREATEDATETIME = db.Column(db.DateTime)
    LOGINNAME = db.Column(db.String(100), nullable=False, unique=True)
    NAME = db.Column(db.String(100))
    PHOTO = db.Column(db.String(200))
    PWD = db.Column(db.String(100))
    SEX = db.Column(db.String(1))
    UPDATEDATETIME = db.Column(db.DateTime)
    EMPLOYDATE = db.Column(db.DateTime)
