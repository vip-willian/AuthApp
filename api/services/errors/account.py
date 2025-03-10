from .base import BaseServiceError


class AccountNotFoundError(BaseServiceError):
    pass


class AccountLoginError(BaseServiceError):
    pass


class AccountPasswordError(BaseServiceError):
    pass