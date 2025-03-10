import base64
import binascii
import hashlib
import re

password_pattern = r"^(?=.*[a-zA-Z])(?=.*\d).{8,}$"


def valid_password(password):
    pattern = password_pattern

    if re.match(pattern, password) is not None:
        return password
    raise ValueError("Password must contain letters and numbers, and the length must be greater than 8.")


def hash_password(password_str, salt_byte):
    dk = hashlib.pbkdf2_hmac("sha256", password_str.encode("utf-8"), salt_byte, 10000)
    return binascii.hexlify(dk)


def compare_password(password_str, password_hashed_base64, slat_base64):
    return hash_password(password_str, base64.b64decode(slat_base64)) == base64.b64decode(password_hashed_base64)
