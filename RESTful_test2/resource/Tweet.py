from flask_restful import Resource, reqparse
from RESTful_test2.model.tweet import Tweet as TweetModel
from RESTful_test2.model.User import User as UserModel
from flask_jwt import jwt_required, current_identity

class Tweet(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "body", type=str, required=True, help='body required'
    )

    @jwt_required()
    def post(self,username):
        if current_identity.username != username:
            return {"message": "please use right token"}
        user = UserModel.get_by_username(username)
        if not user:
            return {"message": "user not found"}, 404

        data = self.parse.parse_args()
        tweet = TweetModel(body=data.get('body'), user_id=user.id)
        tweet.add()
        return tweet.as_dict()


    def get(self,username):
        user = UserModel.get_by_username(username)
        if not user:
            return {"message": "user not found"}, 404
        return [u.as_dict() for u in user.tweet]