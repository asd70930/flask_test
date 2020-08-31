from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

from RESTful_test2.resource.hello import Helloworld
from RESTful_test2.resource.User import User, Userlist
from RESTful_test2.config import Config
from RESTful_test2.resource.auth import Login
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
    # use python class to config app
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)


    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(Userlist, "/users")
    api.add_resource(Login, "/auth/login")
    return app
