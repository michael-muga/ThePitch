import os


class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = '5d3135c3c429dc8d505a0b68'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:mike2020@localhost/thepitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}