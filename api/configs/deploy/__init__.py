from pydantic_settings import BaseSettings
from pydantic import Field


class DeploymentConfig(BaseSettings):
    # 应用名称
    APPLICATION_NAME: str = Field(
        description="Name of the application, used for identification and logging purposes",
        default="vip-willian/AuthApp",
    )

    # 是否开启Debug模式
    DEBUG: bool = Field(
        description="Enable debug mode for additional logging and development features",
        default=False,
    )

    # 是否是教育版本
    EDITION: str = Field(
        description="Deployment edition of the application (e.g., 'SELF_HOSTED', 'CLOUD')",
        default="SELF_HOSTED",
    )

    # 应用部署环境
    DEPLOY_ENV: str = Field(
        description="Deployment environment (e.g., 'PRODUCTION', 'DEVELOPMENT'), default to PRODUCTION",
        default="PRODUCTION",
    )
