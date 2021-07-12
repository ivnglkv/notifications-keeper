from flask import (
    Flask,
)


def create_app(conf: dict = None):
    from .service.app import module as service_module

    app = Flask(__name__)

    if conf is None:
        app.config.from_envvar('HOOK_APP_CONFIG')
    else:
        app.config.from_mapping(conf)

    app.register_blueprint(service_module, url_prefix='/service')

    return app
