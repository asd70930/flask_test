#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from flask import current_app
# from datetime import datetime, timedelta
# import jwt
from RESTful_test2 import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from RESTful_test2.model.base import Base

class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))

    tweet = relationship('Tweet')

    def __repr__(self):
        return "id={} ,name={}".format(self.id, self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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

    # flask-JWT used
    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)
        if user:
            #check password
            if user.check_password(password):
                return user

    # flask-JWT used
    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = User.get_by_id(user_id)
        return user

