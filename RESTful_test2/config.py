from datetime import timedelta
import os

config_path = os.path.abspath(os.path.dirname(__file__))
class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = '/auth/login'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    JWT_SECRET_KEY = 'flask123'
    SQL_URL = os.environ.get("DATABASE_URL")
    SQL_PORT = os.environ.get("DATABASE_PORT")
    SQL_USER = os.environ.get("DATABASE_USER")
    SQL_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/demo' % \
                              (SQL_USER, SQL_PASSWORD, SQL_URL, SQL_PORT)

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///demo.db'
    SECRET_KEY = 'flask123'



class DevelopmentConfig(Config):
    SECRET_KEY = 'flask123'
    SQL_URL = '0.0.0.0'
    SQL_PORT = '3306'
    SQL_USER = 'john'
    SQL_PASSWORD = '123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/demo' % \
                              (SQL_USER, SQL_PASSWORD, SQL_URL, SQL_PORT)



class ProductionConfig(Config):
    SECRET_KEY = 'flask123'


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}