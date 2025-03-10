import jwt
from werkzeug.exceptions import Unauthorized
from api.configs import auth_config

class PassportService:
    def __init__(self):
        self.sk = auth_config.SECRET_KEY

    def issue(self, payload):
        return jwt.encode(payload, self.sk, algorithm='HS256')

    def verify(self, token):
        try:
            return jwt.decode(token, self.sk, algorithm=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            raise Unauthorized("Invalid token signature.")
        except jwt.exceptions.ExpiredSignatureError:
            raise Unauthorized("Token has expired.")
        except jwt.exceptions.DecodeError:
            raise Unauthorized("Invalid token.")
