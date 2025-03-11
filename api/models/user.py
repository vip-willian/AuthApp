from models import db as sql
import sqlalchemy as db


class SysUser(sql.Model):
    __tablename__ = 'sys_user'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '用户信息表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    login_name = db.Column(db.String(100), nullable=False, unique=True, comment='登录名')
    name = db.Column(db.String(100), comment='用户名')
    password = db.Column(db.String(100), comment='密码')
    photo = db.Column(db.String(200), comment='照片')
    sex = db.Column(db.Integer, comment='性别')
    age = db.Column(db.SmallInteger, comment='年龄')
    email = db.Column(db.String(50), server_default=db.FetchedValue(), comment='用户邮箱')
    phone = db.Column(db.String(11), server_default=db.FetchedValue(), comment='手机号码')
    employ_date = db.Column(db.DateTime, comment='雇佣日期')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), comment='用户状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysUserOrganization(sql.Model):
    __tablename__ = 'sys_user_organization'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '用户机构关联表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, comment='用户ID')
    organization_id = db.Column(db.BigInteger, nullable=False, comment='机构ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('user_id', 'organization_id', name='uk_user_organization_id')


class SysUserRole(sql.Model):
    __tablename__ = 'sys_user_role'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '用户角色关联表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, comment='用户ID')
    role_id = db.Column(db.BigInteger, nullable=False, comment='角色ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('user_id', 'role_id', name='uk_user_role_id')
