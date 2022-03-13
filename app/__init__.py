from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos',IMAGES)
mail = Mail()

login_manager.session_protection = 'strong'


def create_app(config_name):

    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])
    #initialising flask extension
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #configure uploads 
    configure_uploads(app,photos)

    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth
    app.register_blueprint(auth, url_prefix = '/')

    return app