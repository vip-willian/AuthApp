import flask_login
import json
from flask_restful import Resource, reqparse, inputs, marshal, fields
from libs.field_validate import field_len_limit
from flask_login import login_required
from typing import cast
from models.user import User
from services.user_service import UserService


class GetUserMenusApi(Resource):

    @login_required
    def get(self):
        user = cast(User, flask_login.current_user)
        return {"code": 200, "message": "ok", "data": UserService.get_user_menus(user=user)}


class GetUserList(Resource):
    def get(self):
        pass


class GetUserById(Resource):
    def get(self, id):
        return {'userId': id}


class UserRegister(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=field_len_limit(8), required=True, help='用户名长度不能超过8个字符', trim=True,
                            location='args')
        parser.add_argument('loginName', type=str, required=True, help='登录名不能为空', trim=True, location='args')
        parser.add_argument('password', type=field_len_limit(10), required=True, help='密码不能超过10个字符', trim=True,
                            location='args')
        parser.add_argument('photo', type=str, required=False, trim=True,
                            location='args')
        parser.add_argument('sex', type=inputs.int_range(0, 1), help='性别范围不合法', required=False,
                            location='args')
        parser.add_argument('age', type=inputs.int_range(0, 200), help='年龄范围在1-200之间', required=False,
                            location='args')
        parser.add_argument('email',
                            type=inputs.regex(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'),
                            required=True, help='邮箱格式不正确', trim=True,
                            location='args')
        parser.add_argument('phone', type=inputs.regex(r'1(3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[0-35-9])\d{8}'),
                            required=True, help='手机号格式不正确', trim=True,
                            location='args')
        parser.add_argument('employDate', type=inputs.date, required=False, help='非法的雇佣日期格式', trim=True,
                            location='args')

        args = parser.parse_args()

        user_register_fields = {
            'email': fields.String,
            'phone': fields.String
        }

        return {'code': 200, 'data': marshal(
            args, user_register_fields
        )}
