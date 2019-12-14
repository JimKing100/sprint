""" SQLAlchemy models for Test """

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """ Test Data """
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)
