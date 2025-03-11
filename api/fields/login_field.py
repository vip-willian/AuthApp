from flask_restful import fields

current_user_detail_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "phone": fields.String,
    "last_login_ip": fields.String,
}