import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from flask import request
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_babel import Babel
# from flask_bootstrap import Bootstrap
from config import Config
from flask_static_digest import FlaskStaticDigest

db = SQLAlchemy()
# bootstrap = Bootstrap()
migrate = Migrate()
moment = Moment()
babel = Babel()
flask_static_digest = FlaskStaticDigest()


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, static_folder='public/', static_url_path='')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    # bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    flask_static_digest.init_app(app)
    # TODO: Make these optional with env var
    # login.init_app(app)
    # mail.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # TODO: Make this optional with env var
    # from app.auth import bp as auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')

    if not app.debug and not app.testing:
        # Log Setting
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('App startup')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


@babel.localeselector
def get_locale():
    # Comment/Uncomment the next two lines to test i18n and l10n
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
    # return 'es'


# must remain at bottom of file.
from app import models

