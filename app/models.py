from enum import unique
from sqlalchemy import PrimaryKeyConstraint
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.Strring(250), unique = True)
    password = db.Column(db.String(250))
    username = db.Column(db.String(250))

    def __repr__(self):
        return f"User('{self.firstname}')"

class Pitch(db.Model):
    '''
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'Pitch {self.description}'

class Comment(db.Model):
    '''
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(255), index=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f'Comment {self.content}'