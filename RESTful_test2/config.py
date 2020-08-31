

class Config():
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = 'flask123'
