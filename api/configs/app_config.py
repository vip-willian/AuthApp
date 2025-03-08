from pydantic_settings import SettingsConfigDict

from .middleware import MiddlewareConfig
from .packaging import PackagingInfo
from .deploy import DeploymentConfig
from .enterprise import EnterpriseFeatureConfig

class AuthConfig(
    PackagingInfo,
    DeploymentConfig,
    MiddlewareConfig,
    EnterpriseFeatureConfig):

    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file='.env',
        env_file_encoding='utf-8',
        # ignore extra attributes
        extra ="ignore"
    )
