#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from flask import current_app
# from datetime import datetime, timedelta
# import jwt
from RESTful_test2 import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))

    tweet = relationship('Tweet')

    def __repr__(self):
        return "id={} ,name={}".format(self.id, self.name)

    def as_dict(self):
        # print(self.__table__.columns)
        """
        ['user.id', 'user.name', 'user.email', 'user.password_hash']
        直接去翻SQLAlchemy無法找到__table__ , 但確實有這個屬性
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(
            User.name == username
        ).first()

    @staticmethod
    def get_by_id(id):
        return db.session.query(User).filter(
            User.id == id
        ).first()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)
        if user:
            #check password
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = User.get_by_id(user_id)
        return user
    # def generate_token(self):
    #     """
    #     Generate the access token
    #
    #     :return:
    #     """
    #     try:
    #         # set up a payload with an expiration time
    #         payload = {
    #             "exp": datetime.utcnow() + timedelta(minutes=5),
    #             "iat": datetime.utcnow(),
    #             "sub": self.name
    #         }
    #
    #         jwt_token = jwt.encode(
    #             payload,
    #             current_app.config.get('SECRET_KEY'),
    #             algorithm="HS256"
    #         )
    #         return jwt_token.decode()
    #
    #     except Exception as e:
    #         return str(e)
