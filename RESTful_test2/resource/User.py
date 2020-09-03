from flask_restful import Resource, reqparse
from RESTful_test2.model.User import User as UserModel
from flask_jwt import jwt_required

def min_length_strP(min_length):
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


def min_length_strE(min_length):
    def validate(s):
        if s is None:
            raise Exception('password is required')
        if not isinstance(s, (int,str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >=min_length:
            return s
        else:
            #
            raise Exception('email must be at least %i characters long' % min_length)
    return validate


class User(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "password", type=min_length_strP(5), required=True, help='{error_msg}'
    )
    parse.add_argument(
        "email", type=min_length_strE(5), required=True, help='{error_msg}'
    )
    def get(self, username):
        """
        get a user detail information
        """
        user = UserModel.get_by_username(username)
        if user:
            return user.as_dict()
        return {"message": "user not found"}, 404

    def post(self, username):
        """
        create a user
        """
        data = self.parse.parse_args()
        user = UserModel.get_by_username(username)
        if user:
            return {"message": "user already exist"}
        user = UserModel(
            name=username,
            email=data.get('email')
        )
        user.set_password(data.get('password'))
        user.add()
        return user.as_dict()


    def delete(self, username):
        """
        delete a user
        """
        user = UserModel.get_by_username(username)
        if user:
            user.delete()
            return {"message": "user delete done"}
        return {"message": "user not found"}, 404

    def put(self, username):
        """
        update a user detail information
        return code 204 can't show message body
        if you want to show message body, return code 200 and write return message
        """
        user = UserModel.get_by_username(username)
        if user:
            data = self.parse.parse_args()
            user.email = data.get('email')
            user.set_password(data.get('password'))
            user.update()
            return user.as_dict()
        return {"message": "user not found"}



class Userlist(Resource):

    @jwt_required()
    def get(self):
        users = UserModel.get_user_list()
        return [u.as_dict() for u in users]

