import enum
from .engine import db
from flask_login import UserMixin
from models.base import BaseModel

class UserStatus(enum.StrEnum):
    PENDING = "pending"
    UNINITIALIZED = "uninitialized"
    ACTIVE = "active"
    BANNED = "banned"
    CLOSED = "closed"


class MenuType(enum.StrEnum):
    CATALOG = "catalog"  # 目录
    MENU = "menu"  # 菜单


class UserRole(BaseModel):
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


class User(BaseModel, UserMixin):
    __tablename__ = 'sys_user'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '用户表'
    }
    id = db.Column(db.BigInteger, primary_key=True, comment='用户ID')
    username = db.Column(db.String(100), nullable=False, unique=True, comment='用户名')
    alias = db.Column(db.String(100), comment='用户昵称')
    password = db.Column(db.String(255), nullable=False, comment='密码')
    password_salt = db.Column(db.String(255), nullable=False, comment='密码加盐')
    phone = db.Column(db.String(11), nullable=False, comment='手机号码')
    email = db.Column(db.String(50), nullable=True, comment='用户邮箱')
    avatar = db.Column(db.String(255), comment='头像')
    sex = db.Column(db.Integer, comment='性别')
    age = db.Column(db.SmallInteger, comment='年龄')
    tenant_code = db.Column(db.String(8), nullable=False, default='0', comment='租户CODE')
    org_id = db.Column(db.BigInteger, nullable=False, default=0, comment='机构ID')
    dept_id = db.Column(db.BigInteger, nullable=False, default=0, comment='部门ID')
    is_superuser = db.Column(db.Boolean, default=False, comment='是否为超级管理员')
    last_login_at = db.Column(db.DateTime, comment='最近一次登录时间')
    last_login_ip = db.Column(db.String(255), comment='最近一次登录IP')
    last_active_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                               comment='最近一次激活时间')
    user_status = db.Column(db.String(16), nullable=False, default='active', comment='用户状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')

    @property
    def is_active(self):
        return UserStatus.ACTIVE.value == self.user_status

    @property
    def get_role_ids(self) -> list[int]:
        user_roles = (
            db.session.query(UserRole).filter(UserRole.user_id == self.id).all()
        )
        if not user_roles or len(user_roles) == 0:
            return []
        return [x.role_id for x in user_roles]


class Role(BaseModel):
    __tablename__ = 'sys_role'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '角色信息表'
    }
    id = db.Column(db.BigInteger, primary_key=True, comment='角色ID')
    name = db.Column(db.String(100), nullable=False, comment='角色名称')
    desc = db.Column(db.String(200), comment='角色描述')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class Dept(BaseModel):
    __tablename__ = 'sys_dept'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '部门信息表'
    }
    id = db.Column(db.BigInteger, primary_key=True, comment='部门ID')
    parent_id = db.Column(db.BigInteger, default=0, comment='父部门ID')
    org_id = db.Column(db.BigInteger, nullable=False, default=0, comment='机构ID')
    name = db.Column(db.String(100), nullable=False, comment='部门名称')
    order = db.Column(db.SmallInteger(), nullable=False, default=0, comment='排序')
    desc = db.Column(db.String(200), comment='备注')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class Organization(BaseModel):
    __tablename__ = 'sys_organization'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '机构信息表'
    }
    id = db.Column(db.BigInteger, primary_key=True, comment='机构ID')
    name = db.Column(db.String(200), comment='机构名称')
    leader = db.Column(db.String(20), comment='机构负责人')
    phone = db.Column(db.String(11), comment='联系电话')
    email = db.Column(db.String(50), comment='邮箱')
    address = db.Column(db.String(200), comment='机构地址')
    status = db.Column(db.Integer, comment='机构状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class Menu(BaseModel):
    __tablename__ = 'sys_menu'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '菜单信息表'
    }
    id = db.Column(db.BigInteger, primary_key=True, comment='菜单ID')
    parent_id = db.Column(db.BigInteger, default=0, comment='父菜单ID')
    name = db.Column(db.String(100), nullable=False, comment='菜单名称')
    menu_type = db.Column(db.String(16), nullable=False, default='menu', comment='菜单类型')
    icon = db.Column(db.String(100), nullable=True, comment='菜单图标')
    path = db.Column(db.String(100), comment='菜单路径')
    order = db.Column(db.SmallInteger(), nullable=False, default=0, comment='排序')
    remark = db.Column(db.JSON, nullable=True, comment='备注')
    is_hidden = db.Column(db.Boolean, default=False, comment='是否隐藏')
    component = db.Column(db.String(100), nullable=True, comment='组件')
    keepalive = db.Column(db.Boolean, default=True, comment='存活')
    redirect = db.Column(db.String(100), nullable=True, comment='重定向')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ('id', 'parent_id', 'name','menu_type','icon','path','order','remark','is_hidden','component','keepalive','redirect')

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

    @staticmethod
    def get_menus(menu_ids):
        if menu_ids and len(menu_ids) != 0:
            menus = (
                db.session.query(Menu).filter(Menu.id.in_(menu_ids)).all()
            )
            if not menus:
                return []
            return menus
        return []


class RoleMenu(BaseModel):
    __tablename__ = 'sys_role_menu'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '角色菜单关联表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    role_id = db.Column(db.BigInteger, nullable=False, comment='角色ID')
    menu_id = db.Column(db.BigInteger, nullable=False, comment='菜单ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('role_id', 'menu_id', name='uk_role_menu_id')

    @staticmethod
    def get_menus_ids(role_ids: list[int]) -> list[int]:

        if role_ids and len(role_ids) != 0:
            role_menus = (
                db.session.query(RoleMenu).filter(RoleMenu.role_id.in_(role_ids)).all()
            )
            if not role_menus:
                return []
            return [x.menu_id for x in role_menus]
        return []
