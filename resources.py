from app.database_module.models import User, Event, Survey
from app.database_module.db import session
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask import request

user_fields = {
    'username': fields.String,
    'password': fields.String,
    'email': fields.String
}

event_fields = {
    'eventname': fields.String,
    'location': fields.String,
    'start_time': fields.DateTime,
    'end_time': fields.datetime,
    'host': fields.String,
    'address': fields.String,
    'description': fields.String
}

survey_fields = {
    'surveyname' : fields.String,
    'type': fields.String,
    'description': fields.String,
    'eventid': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, location='form')
parser.add_argument('password', type=str, location='form')
parser.add_argument('email', type=str, location='form')


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message='User {} does not exist'.format(id))
        return user,200

    def delete(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message='User {} does not exist'.format(id))
        session.delete(user)
        try:
            session.commit()
        except:
            session.rollback()
        return {}, 204

    @marshal_with(user_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        user = session.query(User).filter(User.id == id).first()
        json_data = request.get_json(format=True)
        user = User(username=json_data['username'],
                    password=json_data['password'],
                    email=json_data['email'])
        session.add(user)
        try:
            session.commit()
        except:
            session.rolllback()
        return user,201

class UserListResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        user = session.query(User).all()
        return user,200

    def post(self):
        json_data = request.get_json(force=True)
        user = User(username=json_data['username'],
                    password=json_data['password'],
                    email=json_data['email'])
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        return 200

class EventResource(Resource):
    @marshal_with(event_fields)
    def get(self, id):
        event = session.query(Event).filter(Event.id == id).first()
        if not event:
            abort(404, message='Event {} does not exist'.format(id))
        return event, 200

    def delete(self, id):
        event = session.query(Event).filter(Event.id == id).first()
        if not event:
            abort(404, message='User {} does not exist'.format(id))
        session.delete(event)
        try:
            session.commit()
        except:
            session.rolllback()
        return {}, 204

    @marshal_with(event_fields)
    def put(self, id):
        event = session.query(Event).filter(Event.id == id).first()
        json_data = request.get_json(format=True)
        event = Event(
                      event_name = json_data["event_name"],
                      location = json_data["location"],
                      start_time = json_data['start_time'],
                      end_time = json_data["end_time"],
                      host = json_data["host"],
                      address = json_data["address"],
                      description = json_data["description"])
        session.add(event)
        try:
            session.commit()
        except:
            session.rollback()
        return event, 201

class EventListResource(Resource):
    @marshal_with(event_fields)
    def get(self):
        event = session.query(Event).all()
        return event,200

    # @marshal_with(user_fields)
    def post(self):
        json_data = request.get_json(force=True)
        event = Event(
                       event_name=json_data["event_name"],
                      location = json_data["location"],
                      start_time = json_data['start_time'],
                      end_time = json_data["end_time"],
                      host = json_data["host"],
                      address = json_data["address"],
                      description = json_data["description"]
                    )
        session.add(event)
        try:
            session.commit()
        except:
            session.rollback()
        return 200

class SurveyResource(Resource):
    @marshal_with(survey_fields)
    def get(self, id):
        survey = session.query(Survey).filter(Survey.id == id).first()
        if not survey:
            abort(404, message='Survey {} does not exist'.format(id))
        return survey, 200

    def delete(self, id):
        survey = session.query(Survey).filter(Survey.id == id).first()
        if not survey:
            abort(404, message='Survey {} does not exist'.format(id))
        session.delete(survey)
        try:
            session.commit()
        except:
            session.rollback()
        return {}, 204

    @marshal_with(survey_fields)
    def put(self, id):
        survey = session.query(Survey).filter(Survey.id == id).first()
        json_data = request.get_json(format=True)
        survey = Survey(surveyname = json_data["surveyname"],
                      type = json_data['type'],
                      description = json_data["description"],
                      eventid = json_data["eventid"]
                    )
        session.add(survey)
        try:
            session.commit()
        except:
            session.rollback()
        return survey, 201

class SurveyListResource(Resource):
    @marshal_with(survey_fields)
    def get(self):
        survey = session.query(Survey).all()
        return survey,200

    # @marshal_with(user_fields)
    def post(self):
        json_data = request.get_json(force=True)
        survey = Survey(survey_name = json_data["surveyname"],
                      type = json_data['type'],
                      description = json_data["description"],
                      eventid = json_data["eventid"]
                    )
        session.add(survey)
        try:
            session.commit()
        except:
            session.rollback()
        return 200