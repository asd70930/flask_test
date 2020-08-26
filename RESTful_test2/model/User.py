#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RESTful_test2 import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "id={} ,name={}".format(self.id, self.name)

    def as_dict(self):
        # print(self.__table__.columns)
        """
        ['user.id', 'user.name', 'user.email', 'user.password_hash']
        直接去翻SQLAlchemy無法找到__table__ , 但確實有這個屬性
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
