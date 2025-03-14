from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

# 重新定制索引名称转换规则
metadata = MetaData(naming_convention=INDEXES_NAMING_CONVENTION)
db = SQLAlchemy(metadata=metadata)
