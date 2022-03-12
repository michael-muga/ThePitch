import os
class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = '5d3135c3c429dc8d505a0b68'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:mike2020@localhost/thepitch'

    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
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