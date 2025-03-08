from api.models import db


class SysOrganization(db.Model):
    __tablename__ = 'sys_organization'

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    organization_id = db.Column(db.BigInteger, index=True, info='机构ID')
    code = db.Column(db.String(200), info='机构编码')
    icon = db.Column(db.String(100), info='图标')
    name = db.Column(db.String(200), info='机构名称')
    seq = db.Column(db.Integer, info='序号')
    leader = db.Column(db.String(20), info='负责人')
    phone = db.Column(db.String(11), info='联系电话')
    email = db.Column(db.String(50), info='邮箱')
    address = db.Column(db.String(200), info='地址')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')


class SysOrganizationResource(db.Model):
    __tablename__ = 'sys_organization_resource'
    __table_args__ = (
        db.Index('uk_organization_resource_id', 'organization_id', 'resource_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True, info='主键ID')
    organization_id = db.Column(db.BigInteger, nullable=False, info='机构ID')
    resource_id = db.Column(db.String(36), nullable=False, info='资源ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
