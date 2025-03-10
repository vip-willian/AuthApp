from pydantic_settings import BaseSettings
from pydantic import Field, PositiveInt, PositiveFloat
from typing import Optional


class SecurityConfig(BaseSettings):
    SECRET_KEY: str = Field(
        description="Secret key for secure session cookie signing."
                    "Make sure you are changing this key for your deployment with a strong key."
                    "Generate a strong key using `openssl rand -base64 42` or set via the `SECRET_KEY` environment variable.",
        default="",
    )


class AuthConfig(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: PositiveInt = Field(
        description="Expiration time for access tokens in minutes",
        default=60,
    )

    REFRESH_TOKEN_EXPIRE_DAYS: PositiveFloat = Field(
        description="Expiration time for refresh tokens in days",
        default=30,
    )

    LOGIN_LOCKOUT_DURATION: PositiveInt = Field(
        description="Time (in seconds) a user must wait before retrying login after exceeding the rate limit.",
        default=86400,
    )

    FORGOT_PASSWORD_LOCKOUT_DURATION: PositiveInt = Field(
        description="Time (in seconds) a user must wait before retrying password reset after exceeding the rate limit.",
        default=86400,
    )


class LoggingConfig(BaseSettings):
    """
    Configuration for application logging
    """

    LOG_LEVEL: str = Field(
        description="Logging level, default to INFO. Set to ERROR for production environments.",
        default="INFO",
    )

    LOG_FILE: Optional[str] = Field(
        description="File path for log output.",
        default=None,
    )

    LOG_FILE_MAX_SIZE: PositiveInt = Field(
        description="Maximum file size for file rotation retention, the unit is megabytes (MB)",
        default=20,
    )

    LOG_FILE_BACKUP_COUNT: PositiveInt = Field(
        description="Maximum file backup count file rotation retention",
        default=5,
    )

    LOG_FORMAT: str = Field(
        description="Format string for log messages",
        default="%(asctime)s.%(msecs)03d %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s",
    )

    LOG_DATEFORMAT: Optional[str] = Field(
        description="Date format string for log timestamps",
        default=None,
    )

    LOG_TZ: Optional[str] = Field(
        description="Timezone for log timestamps (e.g., 'America/New_York')",
        default="UTC",
    )


# 业务功能配置
class FeatureConfig(
    # 安全配置
    SecurityConfig,
    # 登录授权配置
    AuthConfig,
    # 日志配置
    LoggingConfig):
    pass
