from libs.exception import BaseHTTPException


class UserBannedError(BaseHTTPException):
    error_code = "user_banned"
    description = "User is banned."
    code = 400

class UserNotFound(BaseHTTPException):
    error_code = "user_not_found"
    description = "User not found."
    code = 400

class UserNameOrPasswordMismatchError(BaseHTTPException):
    error_code = "username_or_password_mismatch"
    description = "The username or password is mismatched."
    code = 400
