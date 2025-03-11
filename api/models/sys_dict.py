from models import db as sql
import sqlalchemy as db


class SysDictData(sql.Model):
    __tablename__ = 'sys_dict_data'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '系统字典数据表'
    }

    dict_code = db.Column(db.BigInteger, primary_key=True, comment='字典编码')
    dict_sort = db.Column(db.Integer, server_default=db.FetchedValue(), comment='字典排序')
    dict_label = db.Column(db.String(100), server_default=db.FetchedValue(), comment='字典标签')
    dict_value = db.Column(db.String(100), server_default=db.FetchedValue(), comment='字典键值')
    dict_type = db.Column(db.String(100), index=True, server_default=db.FetchedValue(), comment='字典类型')
    css_class = db.Column(db.String(100), comment='样式属性（其他样式扩展）')
    list_class = db.Column(db.String(100), comment='表格回显样式')
    is_default = db.Column(db.String(1), server_default=db.FetchedValue(), comment='是否默认（Y是 N否）')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), comment='状态（0正常 1停用）')
    remark = db.Column(db.String(500), comment='备注')
    create_by = db.Column(db.String(64), server_default=db.FetchedValue(), comment='创建者')
    update_by = db.Column(db.String(64), server_default=db.FetchedValue(), comment='更新者')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysDictType(sql.Model):
    __tablename__ = 'sys_dict_type'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '字典类型表'
    }

    dict_id = db.Column(db.BigInteger, primary_key=True, comment='字典主键')
    dict_name = db.Column(db.String(100), server_default=db.FetchedValue(), comment='字典名称')
    dict_type = db.Column(db.String(100), unique=True, server_default=db.FetchedValue(), comment='字典类型')
    remark = db.Column(db.String(500), comment='备注')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), comment='状态（0正常 1停用）')
    create_by = db.Column(db.String(64), server_default=db.FetchedValue(), comment='创建者')
    update_by = db.Column(db.String(64), server_default=db.FetchedValue(), comment='更新者')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysConfig(sql.Model):
    __tablename__ = 'sys_config'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '系统配置表'
    }

    config_id = db.Column(db.BigInteger, primary_key=True, comment='参数主键')
    config_name = db.Column(db.String(100), server_default=db.FetchedValue(), comment='参数名称')
    config_key = db.Column(db.String(100), server_default=db.FetchedValue(), comment='参数键名')
    config_value = db.Column(db.String(500), server_default=db.FetchedValue(), comment='参数键值')
    config_type = db.Column(db.String(1), server_default=db.FetchedValue(), comment='系统内置（Y是 N否）')
    remark = db.Column(db.String(500), comment='备注')
    create_by = db.Column(db.String(64), server_default=db.FetchedValue(), comment='创建者')
    update_by = db.Column(db.String(64), server_default=db.FetchedValue(), comment='更新者')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')


class SysOnline(sql.Model):
    __tablename__ = 'sys_online'
    __table_args__ = {
        "mysql_charset": "utf8",
        'comment': '用户在线信息表'
    }

    id = db.Column(db.BigInteger, primary_key=True, comment='主键ID')
    ip = db.Column(db.String(100), comment='登录IP')
    login_name = db.Column(db.String(100), comment='登录名')
    type = db.Column(db.Integer, comment='类型')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='创建时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                             comment='更新时间')
