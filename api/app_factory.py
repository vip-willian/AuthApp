from auth_app import AuthApp
from configs import auth_config
import time
import logging


def create_app_with_config() -> AuthApp:
    app = AuthApp(__name__)
    # 加载配置
    app.config.from_mapping(auth_config.model_dump())
    return app


def initialize_extensions(app: AuthApp):
    from api.extensions import ext_blueprints, ext_database

    extensions = [
        ext_blueprints,
        ext_database
    ]

    for ext in extensions:
        short_name = ext.__name__.split(".")[-1]
        is_enabled = ext.is_enabled() if hasattr(ext, "is_enabled") else True
        if not is_enabled:
            if auth_config.DEBUG:
                logging.info(f"Skipped {short_name}")
            continue

        start_time = time.perf_counter()
        ext.init_app(app)
        end_time = time.perf_counter()
        if auth_config.DEBUG:
            logging.info(f"Loaded {short_name} ({round((end_time - start_time) * 1000, 2)} ms)")


def create_app() -> AuthApp:
    start_time = time.perf_counter()
    app = create_app_with_config()
    initialize_extensions(app)
    end_time = time.perf_counter()
    if auth_config.DEBUG:
        logging.info(f"Finished create_app ({round((end_time - start_time) * 1000, 2)} ms)")
    return app

def create_migrations_app() -> AuthApp:
    app = create_app_with_config()
    from extensions import ext_database,ext_migrate

    # Initialize only required extensions
    ext_database.init_app(app)
    ext_migrate.init_app(app)
    return app

