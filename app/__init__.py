from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])
    #initialising flask extension
    bootstrap.init_app(app)

    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app