from models import db as sql
import sqlalchemy as db


class SysOrganization(sql.Model):
    __tablename__ = 'sys_organization'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '机构信息表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    organization_id = db.Column(db.BigInteger, index=True, comment='机构ID')
    code = db.Column(db.String(200), comment='机构编码')
    icon = db.Column(db.String(100), comment='图标')
    name = db.Column(db.String(200), comment='机构名称')
    seq = db.Column(db.Integer, comment='序号')
    leader = db.Column(db.String(20), comment='负责人')
    phone = db.Column(db.String(11), comment='联系电话')
    email = db.Column(db.String(50), comment='邮箱')
    address = db.Column(db.String(200), comment='地址')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), comment='状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysOrganizationResource(sql.Model):
    __tablename__ = 'sys_organization_resource'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '机构资源关联表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    organization_id = db.Column(db.BigInteger, nullable=False, comment='机构ID')
    resource_id = db.Column(db.String(36), nullable=False, comment='资源ID')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
    db.UniqueConstraint('organization_id', 'resource_id', name='uk_organization_resource_id')
