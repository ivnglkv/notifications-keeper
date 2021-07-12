from flask import (
    Flask,
)


def create_app():
    from .service.app import module as service_module

    app = Flask(__name__)
    app.config.from_envvar('HOOK_APP_CONFIG')

    app.register_blueprint(service_module, url_prefix='/service')

    return app
