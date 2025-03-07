from auth_app import AuthApp
import time
import logging


def create_app_with_config() -> AuthApp:
    app = AuthApp(__name__)
    # 加载配置
    return app


def initialize_extensions(app: AuthApp):
    from api.extensions import ext_blueprints

    extensions = [
        ext_blueprints
    ]

    for ext in extensions:
        short_name = ext.__name__.split(".")[-1]
        is_enabled = ext.is_enabled() if hasattr(ext, "is_enabled") else True
        if not is_enabled:
            logging.info(f"Skipped {short_name}")
            continue

        start_time = time.perf_counter()
        ext.init_app(app)
        end_time = time.perf_counter()
        logging.info(f"Loaded {short_name} ({round((end_time - start_time) * 1000, 2)} ms)")


def create_app() -> AuthApp:
    start_time = time.perf_counter()
    app = create_app_with_config()
    initialize_extensions(app)
    end_time = time.perf_counter()
    logging.info(f"Finished create_app ({round((end_time - start_time) * 1000, 2)} ms)")
    return app
