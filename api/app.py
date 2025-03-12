import sys
from flask_cors import CORS

from models.user import User, Role,Organization,Dept,Menu,UserRole,RoleMenu


def is_db_command():
    if len(sys.argv) > 1 and sys.argv[0].endswith("flask") and sys.argv[1] == "db":
        return True
    return False


if is_db_command():
    from app_factory import create_migrations_app

    app = create_migrations_app()
else:
    from app_factory import create_app

    app = create_app()

if __name__ == '__main__':
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.run(host='0.0.0.0', port=5002, debug=False)
