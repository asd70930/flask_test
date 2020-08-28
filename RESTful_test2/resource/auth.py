from flask_restful import Resource, reqparse
from RESTful_test2 import db
from RESTful_test2.model.User import User as UserModel

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


class Login(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "password", type=str, required=True, help='{error_msg}'
    )
    parse.add_argument(
        "username", type=str, required=True, help='require username'
    )

    def post(self):
        data = self.parse.parse_args()
        user = db.session.query(UserModel).filter(
            UserModel.name == data.get('username')
        ).first()
        if user:
            # auth user
            if not user.check_password(data.get('password')):
                return {"message": "login failed, please input the right username or password"}
            return {
                "message": "login success",
                "token": user.generate_token()
            }
        else:
            return {
                "message": "user not found "
            }


