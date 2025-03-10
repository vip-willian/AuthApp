import os
from pydantic_settings import BaseSettings
from pydantic import Field, NonNegativeInt, computed_field
from typing import Any
from urllib.parse import quote_plus
from .redis_config import RedisConfig


class DatabaseConfig(BaseSettings):
    # 数据库主机
    DB_HOST: str = Field(
        description="Hostname or IP address of the database server.",
        default="localhost",
    )
    # 数据库端口
    DB_PORT: int = Field(
        description="Port number for database connection.",
        default=3306,
    )
    # 数据库用户名
    DB_USERNAME: str = Field(
        description="Username for database authentication.",
        default="root",
    )

    # 数据库密码
    DB_PASSWORD: str = Field(
        description="Password for database authentication.",
        default="123456",
    )

    # 数据库名称
    DB_DATABASE: str = Field(
        description="Name of the database to connect to.",
        default="db_auth",
    )

    DB_CHARSET: str = Field(
        description="Character set for database connection.",
        default="",
    )

    DB_EXTRAS: str = Field(
        description="Additional database connection parameters. Example: 'keepalives_idle=60&keepalives=1'",
        default="",
    )

    SQLALCHEMY_DATABASE_URI_SCHEME: str = Field(
        description="Database URI scheme for SQLAlchemy connection.",
        default="mysql",
    )

    # 组装数据库连接配置
    @computed_field
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        db_extras = (
            f"{self.DB_EXTRAS}&client_encoding={self.DB_CHARSET}" if self.DB_CHARSET else self.DB_EXTRAS
        ).strip("&")
        db_extras = f"?{db_extras}" if db_extras else ""
        return (
            f"{self.SQLALCHEMY_DATABASE_URI_SCHEME}://"
            f"{quote_plus(self.DB_USERNAME)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"
            f"{db_extras}"
        )

    SQLALCHEMY_POOL_SIZE: NonNegativeInt = Field(
        description="Maximum number of database connections in the pool.",
        default=30,
    )

    SQLALCHEMY_MAX_OVERFLOW: NonNegativeInt = Field(
        description="Maximum number of connections that can be created beyond the pool_size.",
        default=10,
    )

    SQLALCHEMY_POOL_RECYCLE: NonNegativeInt = Field(
        description="Number of seconds after which a connection is automatically recycled.",
        default=3600,
    )

    SQLALCHEMY_POOL_PRE_PING: bool = Field(
        description="If True, enables connection pool pre-ping feature to check connections.",
        default=False,
    )

    SQLALCHEMY_ECHO: bool | str = Field(
        description="If True, SQLAlchemy will log all SQL statements.",
        default=False,
    )

    RETRIEVAL_SERVICE_EXECUTORS: NonNegativeInt = Field(
        description="Number of processes for the retrieval service, default to CPU cores.",
        default=os.cpu_count(),
    )

    # 组装连接池配置
    @computed_field
    def SQLALCHEMY_ENGINE_OPTIONS(self) -> dict[str, Any]:
        return {
            "pool_size": self.SQLALCHEMY_POOL_SIZE,
            "max_overflow": self.SQLALCHEMY_MAX_OVERFLOW,
            "pool_recycle": self.SQLALCHEMY_POOL_RECYCLE,
            "pool_pre_ping": self.SQLALCHEMY_POOL_PRE_PING,
            "connect_args": {"options": "-c timezone=UTC"},
        }


class MiddlewareConfig(DatabaseConfig, RedisConfig):
    pass
