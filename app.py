from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


user_list = []

class Helloworld(Resource):
    def get(self):
        return 'Hello World'


class User(Resource):
    def get(self, username):
        """
        get a user detail
        """
        for user in user_list:
            if user['username'] == username:
                return user

    def post(self,username):
        """
        create a user
        """
        user = {
            "username": username,
            "password": request.get_json().get('password')
        }
        user_list.append(user)
        return user


api.add_resource(Helloworld, '/')
api.add_resource(User, '/user/<string:username>')


if __name__ == "__main__":
    app.run()


