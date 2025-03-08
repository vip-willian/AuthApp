from api.models import db


class SysUser(db.Model):
    __tablename__ = 'sys_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    login_name = db.Column(db.String(100), nullable=False, unique=True, info='登录名')
    name = db.Column(db.String(100), info='用户名')
    password = db.Column(db.String(100), info='密码')
    photo = db.Column(db.String(200), info='照片')
    sex = db.Column(db.Integer, info='性别')
    age = db.Column(db.SmallInteger, info='年龄')
    email = db.Column(db.String(50), server_default=db.FetchedValue(), info='用户邮箱')
    phone = db.Column(db.String(11), server_default=db.FetchedValue(), info='手机号码')
    employ_date = db.Column(db.DateTime, info='雇佣日期')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='用户状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')


class SysUserOrganization(db.Model):
    __tablename__ = 'sys_user_organization'
    __table_args__ = (
        db.Index('uk_user_organization_id', 'user_id', 'organization_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    organization_id = db.Column(db.BigInteger, nullable=False, info='机构ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')


class SysUserRole(db.Model):
    __tablename__ = 'sys_user_role'
    __table_args__ = (
        db.Index('uk_user_role_id', 'user_id', 'role_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    user_id = db.Column(db.BigInteger, nullable=False, info='用户ID')
    role_id = db.Column(db.BigInteger, nullable=False, info='角色ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
