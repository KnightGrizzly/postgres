from flask import Flask
from src.config import Config


def create_app():
    """Створює та налаштовує Flask додаток"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Реєстрація Blueprint'ів
    from src.routes.main import main_bp
    from src.routes.users import users_bp
    from src.routes.events import events_bp
    from src.routes.tickets import tickets_bp
    from src.routes.queries import queries_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(queries_bp)

    return app