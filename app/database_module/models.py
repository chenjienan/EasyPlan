from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    email = Column(String(255), unique=True)
    birthday = Column(DateTime)
    avatar = Column(LargeBinary)

    def __init__(self, name=None, password=None, email=None):
        self.username = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Event(Base):
    __tablename__ = 'event'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    event_name = Column(String(255))
    location = Column(String(255))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    host = Column(String(255))
    address = Column(String(255))
    description = Column(String(255))

    def __init__(self, name=None):
        self.event_name = name

    def __repr__(self):
        return '<Event %r>' % (self.eventname)

class Survey(Base):
    __tablename__ = 'survey'
    __table_args__ = {"useexisting": True}
    id = Column(Integer,primary_key=True)
    survey_name = Column(String(255))
    type = Column(Integer)
    description = Column(String(255))
    event_id = Column(Integer)

    def __init__(self, name=None):
        self.survey_name = name

    def __repr__(self):
        return '<Survey %r>' % (self.surveyname)
