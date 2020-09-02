#!/usr/bin/python
# -*- coding: UTF-8 -*-

from RESTful_test2 import db
from sqlalchemy import ForeignKey ,func


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    body = db.Column(db.String(200))
    create_at = db.Colum(db.DateTime, server_default=func.now())

    def __repr__(self):
        return "user_id={}, tweet={}".format(
            self.user_id, self.body
        )



