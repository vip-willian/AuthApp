from werkzeug.routing import ValidationError
import re


def field_len_limit(max_len):
    def validate(s):
        if type(s) != str:
            raise ValidationError("The field must be String.")
        if len(s) <= max_len:
            return s
        raise ValidationError("The field cannot exceed %i characters." % max_len)

    return validate


def email(mail):
    pattern = r"^[\w\.!#$%&'*+\-/=?^_`{|}~]+@([\w-]+\.)+[\w-]{2,}$"
    if re.match(pattern, mail) is not None:
        return mail
    error = f"{mail} is not a valid email address."
    raise ValidationError(error)
