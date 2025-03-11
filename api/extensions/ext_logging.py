import logging
import os
import sys
import uuid
import flask
from auth_app import AuthApp
from configs import auth_config
from logging.handlers import RotatingFileHandler


def init_app(app: AuthApp):
    log_handlers: list[logging.Handler] = []
    log_file = auth_config.LOG_FILE
    if log_file:
        log_dir = os.path.dirname(log_file)
        os.makedirs(log_dir, exist_ok=True)
        log_handlers.append(
            RotatingFileHandler(
                filename=log_file,
                maxBytes=auth_config.LOG_FILE_MAX_SIZE * 1024 * 1024,
                backupCount=auth_config.LOG_FILE_BACKUP_COUNT
            )
        )

    sh = logging.StreamHandler(sys.stdout)
    sh.addFilter(RequestIdFilter())
    log_handlers.append(sh)

    logging.basicConfig(
        level=auth_config.LOG_LEVEL,
        format=auth_config.LOG_FORMAT,
        datefmt=auth_config.LOG_DATE_FORMAT,
        handlers=log_handlers,
        force=True,
    )

    log_tz = auth_config.LOG_TZ
    if log_tz:
        from datetime import datetime
        import pytz

        timezone = pytz.timezone(log_tz)

        def time_converter(seconds):
            return datetime.fromtimestamp(seconds, tz=timezone).timetuple()

        for handler in logging.root.handlers:
            if handler.formatter:
                handler.formatter.converter = time_converter


def get_request_id():
    if getattr(flask.g, "request_id", None):
        return flask.g.request_id
    new_uuid = uuid.uuid4().hex[:10]
    flask.g.request_id = new_uuid
    return flask.g.request_id


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.req_id = get_request_id() if flask.has_request_context() else ""
        return True
