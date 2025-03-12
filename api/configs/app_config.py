from pydantic_settings import SettingsConfigDict

from .middleware import MiddlewareConfig
from .packaging import PackagingInfo
from .deploy import DeploymentConfig
from .enterprise import EnterpriseFeatureConfig
from .feature import FeatureConfig


class AuthConfig(
    PackagingInfo,
    DeploymentConfig,
    MiddlewareConfig,
    FeatureConfig,
    EnterpriseFeatureConfig):
    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file='.env_example',
        env_file_encoding='utf-8',
        # ignore extra attributes
        extra="ignore"
    )
