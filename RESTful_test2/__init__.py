from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

from RESTful_test2.resource.hello import Helloworld
from RESTful_test2.resource.User import User, Userlist

def create_app():
    """
    cmd cd to flask_test not RESTful_test2
    export FlASK_APP="RESTful_test2"
    flask run
    or
    cmd cd to RESTful_test2
    export FlASK_APP=.
    flask run
    """
    app = Flask(__name__)
    api = Api(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1@localhost:3306/demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)


    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(Userlist, "/users")

    return app
