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

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

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

    def __init__(self, event_name=None, location=None, start_time=None, end_time=None, host=None,
                 address=None, description=None):
        self.event_name = event_name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.host = host
        self.address = address
        self.description = description

    def __repr__(self):
        return '<Event %r>' % self.event_name


class Survey(Base):
    __tablename__ = 'survey'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    survey_name = Column(String(255))
    type = Column(Integer)
    description = Column(String(255))
    event_id = Column(Integer)

    def __init__(self, survey_name=None, survey_type=None, description=None, event_id=None):
        self.survey_name = survey_name
        self.type = survey_type
        self.description = description
        self.event_id = event_id

    def __repr__(self):
        return '<Survey %r>' % self.survey_name

