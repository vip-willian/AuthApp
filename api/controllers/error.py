from libs.exception import BaseHTTPException


class AccountBannedError(BaseHTTPException):
    error_code = "account_banned"
    description = "Account is banned."
    code = 400

class AccountNotFound(BaseHTTPException):
    error_code = "account_not_found"
    description = "Account not found."
    code = 400

class EmailOrPasswordMismatchError(BaseHTTPException):
    error_code = "email_or_password_mismatch"
    description = "The email or password is mismatched."
    code = 400
