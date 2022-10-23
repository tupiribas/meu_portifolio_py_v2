from flask import Flask

from portifolio.ext import configuration


def minimal_app():
    app = Flask(__name__)
    configuration.init_app(app)
    return app


def create_app():
    app = minimal_app()
    configuration.init_app(app)
    configuration.carregar_extensoes(app)

    if __name__ == '__main__':
        app.run()
