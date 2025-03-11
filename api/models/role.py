from models import db as sql
import sqlalchemy as db


class SysRole(sql.Model):
    __tablename__ = 'sys_role'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '角色信息表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    seq = db.Column(db.Integer, comment='序号')
    icon = db.Column(db.String(100), comment='图标')
    name = db.Column(db.String(100), nullable=False, comment='角色名称')
    description = db.Column(db.String(200), comment='角色描述')
    role_key = db.Column(db.String(100), nullable=False, comment='角色权限字符串')
    data_scope = db.Column(db.Integer, server_default=db.FetchedValue(),
                           comment='数据范围（1：全部数据权限 2：自定数据权限 3：本部门数据权限 4：本部门及以下数据权限）')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), comment='角色状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysRoleOrganization(sql.Model):
    __tablename__ = 'sys_role_organization'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '角色机构关联表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    role_id = db.Column(db.BigInteger, nullable=False, comment='角色ID')
    organization_id = db.Column(db.BigInteger, nullable=False, comment='机构ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('role_id', 'organization_id', name='uk_role_organization_id')


class SysRoleResource(sql.Model):
    __tablename__ = 'sys_role_resource'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '角色资源关联表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    role_id = db.Column(db.BigInteger, nullable=False, comment='角色ID')
    resource_id = db.Column(db.String(36), nullable=False, comment='资源ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('role_id', 'resource_id', name='uk_role_resource_id')
