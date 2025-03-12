from flask_restful import fields

login_access_token_field = {
    "access_token": fields.String,
    "refresh_token": fields.String,
}

success_field = {
    "code": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(login_access_token_field),
}



current_user_detail_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "is_superuser": fields.Boolean,
    "is_active": fields.Boolean,
    "avatar": fields.String,
    "email": fields.String,
    "phone": fields.String,
    "last_login_ip": fields.String,
}
