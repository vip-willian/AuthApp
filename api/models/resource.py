from models import db as sql
import sqlalchemy as db


class SysResource(sql.Model):
    __tablename__ = 'sys_resource'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '资源信息表'
    }

    id = db.Column(db.String(36), primary_key=True, comment='主键ID')
    resource_id = db.Column(db.String(36), index=True, comment='资源ID')
    resource_type_id = db.Column(db.BigInteger, index=True, comment='资源类型ID')
    seq = db.Column(db.Integer, comment='序号')
    icon = db.Column(db.String(100), comment='图标')
    name = db.Column(db.String(100), nullable=False, comment='名称')
    description = db.Column(db.String(200), comment='描述')
    target = db.Column(db.String(100), comment='目标')
    path = db.Column(db.String(200), comment='路径')
    url = db.Column(db.String(200), comment='URL')
    perms = db.Column(db.String(100), comment='权限标识')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), comment='状态')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysResourceType(sql.Model):
    __tablename__ = 'sys_resource_type'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '资源类型表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    name = db.Column(db.String(100), nullable=False, comment='资源名称')
    description = db.Column(db.String(200), comment='资源描述')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
