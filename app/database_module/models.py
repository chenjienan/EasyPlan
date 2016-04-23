from application import db


class User(db.Model):
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    birthday = db.Column(db.DateTime)
    avatar = db.Column(db.LargeBinary)

    def __init__(self, name=None, password=None, email=None):
        self.username = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    host = db.Column(db.String(255))
    address = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name=None):
        self.event_name = name

    def __repr__(self):
        return '<Event %r>' % (self.eventname)

class Survey(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    survey_name = db.Column(db.String(255))
    type = db.Column(db.Integer)
    description = db.Column(db.String(255))
    event_id = db.Column(db.Integer)

    def __init__(self, name=None):
        self.survey_name = name

    def __repr__(self):
        return '<Survey %r>' % (self.surveyname)
