from sqlalchemy import Column, Integer, String

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = Column(String, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    email = Column(String(120), unique=True)
    birthday = Column(db.DateTime)
    avatar = Column(db.LargeBinary)

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

# class Event(db.Model):
#     __tablename__ = 'event'
#     id = Column(String, primary_key=True)
#     eventname = Column(String(50))
#     location = Column(String(50))
#     starttime = Column(db.dateTime)
#     endtime = Column(db.dateTime)
#     host = Column(String(50))
#     address = Column(String(50))
#     description = Column(String(50))
#
#     def __init__(self, name=None):
#         self.eventname = name
#
#     def __repr__(self):
#         return '<Event %r>' % (self.eventname)
#
# class Survey(db.Model):
#     __tablename__ = 'survey'
#     id = Column(String,primary_key=True)
#     surveyname = Column(String(50))
#     type = Column(Integer)
#     description = Column(String(200))
#     eventid = Column(String(50))
#
#     def __init__(self, name=None):
#         self.surveytname = name
#
#     def __repr__(self):
#         return '<Survey %r>' % (self.surveyname)
#





