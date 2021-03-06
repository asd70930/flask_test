from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT

db = SQLAlchemy()
from RESTful_test2.model.User import User as UserModel
from RESTful_test2.model.tweet import Tweet
from RESTful_test2.resource.hello import Helloworld
from RESTful_test2.resource.User import User, Userlist
from RESTful_test2.resource.Tweet import Tweet
from RESTful_test2.config import app_config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)

def create_app(config_name='development'):
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
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(Userlist, "/users")
    api.add_resource(Tweet, '/tweet/<string:username>')

    # api.add_resource(Login, "/auth/login")
    return app
# gunicorn -w 4 RESTful_test2.wsgi:application
# gunicorn -w 4 -b 0.0.0.0 RESTful_test2.wsgi:application