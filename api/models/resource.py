from api.models import db


class SysResource(db.Model):
    __tablename__ = 'sys_resource'

    id = db.Column(db.String(36), primary_key=True, info='主键ID')
    resource_id = db.Column(db.String(36), index=True, info='资源ID')
    resource_type_id = db.Column(db.BigInteger, index=True, info='资源类型ID')
    seq = db.Column(db.Integer, info='序号')
    icon = db.Column(db.String(100), info='图标')
    name = db.Column(db.String(100), nullable=False, info='名称')
    description = db.Column(db.String(200), info='描述')
    target = db.Column(db.String(100), info='目标')
    path = db.Column(db.String(200), info='路径')
    url = db.Column(db.String(200), info='URL')
    perms = db.Column(db.String(100), info='权限标识')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')


class SysResourceType(db.Model):
    __tablename__ = 'sys_resource_type'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    name = db.Column(db.String(100), nullable=False, info='资源名称')
    description = db.Column(db.String(200), info='资源描述')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
