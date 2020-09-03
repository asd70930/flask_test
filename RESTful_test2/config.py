from datetime import timedelta
import os

config_path = os.path.abspath(os.path.dirname(__file__))
class Config():

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = '/auth/login'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///demo.db'
    SECRET_KEY = 'flask123'



class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost:3306/demo'
    SECRET_KEY = 'flask123'


class ProductionConfig(Config):
    pass


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}