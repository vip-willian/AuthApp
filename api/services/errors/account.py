from .base import BaseServiceError


class UserNotFoundError(BaseServiceError):
    pass


class UserLoginError(BaseServiceError):
    pass


class UserPasswordError(BaseServiceError):
    pass