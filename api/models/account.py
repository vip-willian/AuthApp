from models import db as sql
import sqlalchemy as db
import enum


class AccountStatus(enum.StrEnum):
    PENDING = "pending"
    UNINITIALIZED = "uninitialized"
    ACTIVE = "active"
    BANNED = "banned"
    CLOSED = "closed"


class Account(sql.Model):
    __tablename__ = "account"
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '账号信息表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='账号ID')
    name = db.Column(db.String(255), nullable=False, comment='名称')
    email = db.Column(db.String(255), nullable=False, comment='邮箱')
    phone = db.Column(db.String(11), nullable=False, comment='手机号')
    password = db.Column(db.String(255), nullable=True, comment='密码')
    password_salt = db.Column(db.String(255), nullable=True, comment='密码加盐')
    avatar = db.Column(db.String(255), comment='头衔')
    interface_language = db.Column(db.String(255), comment='语言')
    interface_theme = db.Column(db.String(255), comment='主题')
    timezone = db.Column(db.String(255), comment='时区')
    last_login_at = db.Column(db.DateTime, comment='最近一次登录时间')
    last_login_ip = db.Column(db.String(255), comment='最近一次登录IP')
    last_active_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                               comment='最近一次激活时间')
    status = db.Column(db.String(16), nullable=False, server_default=db.text("'active'"), comment='账号状态')
    initialized_at = db.Column(db.DateTime, comment='初始化日期')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('phone', name='uk_phone')
    db.UniqueConstraint('email', name='uk_email')
