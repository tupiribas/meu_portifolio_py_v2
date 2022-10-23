from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome


def init_app(app):
    Bootstrap(app)
    FontAwesome(app)
