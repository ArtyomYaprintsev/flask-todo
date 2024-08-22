from flask import Flask
from pydantic_core import ValidationError

from server.core import exception_handlers as handlers
from server.core.exceptions import BaseException
from server.config import Config
from server.core.json_provider import CustomJSONProvider

from .tasks.views import tasks


def create_app(config: Config | None = None) -> Flask:
    app = Flask(__name__)

    if config is None:
        config = Config()

    # Set configuration
    app.config.from_object(config)

    # Override default JSON provider
    app.json = CustomJSONProvider(app)

    # Register blueprints
    app.register_blueprint(tasks)

    # Register exception handlers
    app.register_error_handler(
        ValidationError,
        handlers.handle_pydantic_validation_error,
    )
    app.register_error_handler(
        BaseException,
        handlers.handle_base_exception,
    )

    return app
