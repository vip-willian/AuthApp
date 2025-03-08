from api.models import db


class SysRole(db.Model):
    __tablename__ = 'sys_role'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    seq = db.Column(db.Integer, info='序号')
    icon = db.Column(db.String(100), info='图标')
    name = db.Column(db.String(100), nullable=False, info='角色名称')
    description = db.Column(db.String(200), info='角色描述')
    role_key = db.Column(db.String(100), nullable=False, info='角色权限字符串')
    data_scope = db.Column(db.Integer, server_default=db.FetchedValue(),
                           info='数据范围（1：全部数据权限 2：自定数据权限 3：本部门数据权限 4：本部门及以下数据权限）')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='角色状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')


class SysRoleOrganization(db.Model):
    __tablename__ = 'sys_role_organization'
    __table_args__ = (
        db.Index('uk_role_organization_id', 'role_id', 'organization_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    role_id = db.Column(db.BigInteger, nullable=False, info='角色ID')
    organization_id = db.Column(db.BigInteger, nullable=False, info='机构ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')


class SysRoleResource(db.Model):
    __tablename__ = 'sys_role_resource'
    __table_args__ = (
        db.Index('uk_role_resource_id', 'role_id', 'resource_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    role_id = db.Column(db.BigInteger, nullable=False, info='角色ID')
    resource_id = db.Column(db.String(36), nullable=False, info='资源ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
