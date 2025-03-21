# 整合flask_login登录
import json
import logging

import flask_login
from flask import request, Response
from flask_login import user_logged_in, user_loaded_from_request
from contexts import tenant_id
from auth_app import AuthApp
from werkzeug.exceptions import Unauthorized

from libs.passport import PassportService
from services.login_auth_service import LoginAuthService

login_manager = flask_login.LoginManager()


@login_manager.request_loader
def load_user_from_request(request_from_flask_login):
    # jwt token认证拦截
    auth_header = request.headers.get("Authorization", "")
    if not auth_header:
        auth_token = request.args.get("_token")
        if not auth_token:
            raise Unauthorized("Invalid Authorization token.")
    else:
        if " " not in auth_header:
            raise Unauthorized("Invalid Authorization header format. Expected 'Bearer <api-key>' format.")
        auth_scheme, auth_token = auth_header.split(None, 1)
        auth_scheme = auth_scheme.lower()
        if auth_scheme != "bearer":
            raise Unauthorized("Invalid Authorization header format. Expected 'Bearer <api-key>' format.")

    decoded = PassportService().verify(auth_token)
    user_id = decoded.get("user_id")

    logged_in_account = LoginAuthService.load_in_account(user_id=user_id)
    return logged_in_account


@user_logged_in.connect
@user_loaded_from_request.connect
def on_user_logged_in(_sender, user):
    # if user:
    #     tenant_id.set(user.current_tenant_id)
    logging.info(user)
    pass


@login_manager.unauthorized_handler
def unauthorized_handler():
    return Response(
        json.dumps({"code": "unauthorized", "message": "Unauthorized."}),
        status=401,
        content_type="application/json",
    )


def init_app(app: AuthApp):
    login_manager.init_app(app)
