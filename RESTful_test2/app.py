from flask import Flask
from flask_restful import Api
from resource.hello import Helloworld
from resource.User import User, Userlist


app = Flask(__name__)
api = Api(app)


api.add_resource(Helloworld, '/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(Userlist, "/users")

if __name__ == "__main__":
    app.run()


