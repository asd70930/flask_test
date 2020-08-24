from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


user_list = []


def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password is required')
        if not isinstance(s, (int,str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >=min_length:
            return s
        else:
            raise Exception('password must be at least %i characters long' % min_length)
    return validate

class Helloworld(Resource):
    def get(self):
        return 'Hello World'


class User(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "password", type=min_length_str(5), required=True, help='{error_msg}'
    )

    def get(self, username):
        """
        get a user detail information
        """
        for user in user_list:
            if user['username'] == username:
                return user
        return {"message": "user not found"}, 404
    def post(self, username):
        """
        create a user
        """
        data = User.parse.parse_args()
        user = {
            "username": username,
            "password": data.get('password')
        }
        for userr in user_list:
            if userr["username"] == username:
                return {"message": "user already exist"}
        user_list.append(user)
        return user, 201
    def delete(self, username):
        """
        delete a user
        """
        for i, userr in enumerate(user_list):
            if userr["username"] == username:
                del user_list[i]
                return {"message": "user delete done"}
        return {"message": "user not found"}, 204

    def put(self, username):
        """
        update a user detail information
        return code 204 can't show message body
        if you want to show message body, return code 200 and write return message
        """
        data = User.parse.parse_args()
        for i, user in enumerate(user_list):
            if user['username'] == username:
                user_list[i]['password'] = data.get('password')
                return user
        # return {"message": "user not found"}, 204
        return {"message": "user not found"}


class Userlist(Resource):
    def get(self):
        return user_list

api.add_resource(Helloworld, '/')
api.add_resource(User, '/user/<string:username>')
api.add_resource(Userlist, "/users")

if __name__ == "__main__":
    app.run()


