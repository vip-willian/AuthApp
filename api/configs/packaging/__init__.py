from pydantic_settings import BaseSettings
from pydantic import Field


class PackagingInfo(BaseSettings):

    CURRENT_VERSION: str = Field(
        description="Auth Version",
        default="1.0.0",
    )

    COMMIT_SHA: str = Field(
        description="SHA-1 checksum of the git commit used to build the app",
        default="",
    )
