from RESTful_test2 import db



class Base(db.Model):

    __abstract__ = True

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def as_dict(self):
        # print(self.__table__.columns)
        """
        ['user.id', 'user.name', 'user.email', 'user.password_hash']
        直接去翻SQLAlchemy無法找到__table__ , 但確實有這個屬性
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}