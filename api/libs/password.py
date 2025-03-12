import base64
import binascii
import hashlib
import re
import secrets

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


def gen_password(password: str):
    # 获取加盐字符串
    salt = secrets.token_bytes(16)
    # 将加盐字符串进行base64编码
    base64_salt = base64.b64encode(salt).decode()
    # 将密码进行加盐之后hash
    password_hashed = hash_password(password, salt)
    # 将hash之后的密码进行bas4编码
    base64_password_hashed = base64.b64encode(password_hashed).decode()
    print(base64_password_hashed)
    print(base64_salt)
