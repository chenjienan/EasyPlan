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
    'event_name': fields.String,
    'location': fields.String,
    'start_time': fields.DateTime,
    'end_time': fields.datetime,
    'host': fields.String,
    'address': fields.String,
    'description': fields.String
}

survey_fields = {
    'survey_name': fields.String,
    'type': fields.String,
    'description': fields.String,
    'event_id': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, location='form')
parser.add_argument('password', type=str, location='form')
parser.add_argument('email', type=str, location='form')


def delete(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        abort(404, message='User {} does not exist'.format(user_id))
    session.delete(user)
    try:
        session.commit()
    except:
        session.rollback()
    return {}, 204


class UserResource(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            abort(404, message='User {} does not exist'.format(user_id))
        return user, 200

    @marshal_with(user_fields)
    def put(self, user_id):
        # parsed_args = parser.parse_args()
        user = session.query(User).filter(User.id == user_id).first()
        json_data = request.get_json(format=True)
        user = User(username=json_data['username'],
                    password=json_data['password'],
                    email=json_data['email'])
        session.add(user)
        try:
            session.commit()
        except:
            session.rolllback()
        return user, 201


class UserListResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        user = session.query(User).all()
        return user, 200

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
    def get(self, event_id):
        event = session.query(Event).filter(Event.id == event_id).first()
        if not event:
            abort(404, message='Event {} does not exist'.format(event_id))
        return event, 200

    def delete(self, event_id):
        event = session.query(Event).filter(Event.id == event_id).first()
        if not event:
            abort(404, message='User {} does not exist'.format(event_id))
        delete(event)
        try:
            session.commit()
        except:
            session.rolllback()
        return {}, 204

    @marshal_with(event_fields)
    def put(self, event_id):
        event = session.query(Event).filter(Event.id == event_id).first()
        json_data = request.get_json(format=True)
        event = Event(
                      event_name=json_data["event_name"],
                      location=json_data["location"],
                      start_time=json_data['start_time'],
                      end_time=json_data["end_time"],
                      host=json_data["host"],
                      address=json_data["address"],
                      description=json_data["description"])
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
        return event, 200

    # @marshal_with(user_fields)
    def post(self):
        json_data = request.get_json(force=True)
        event = Event(
            event_name=json_data["event_name"],
            location=json_data["location"],
            start_time=json_data['start_time'],
            end_time=json_data["end_time"],
            host=json_data["host"],
            address=json_data["address"],
            description=json_data["description"]
                    )
        session.add(event)
        try:
            session.commit()
        except:
            session.rollback()
        return 200


class SurveyResource(Resource):
    @marshal_with(survey_fields)
    def get(self, survey_id):
        survey = session.query(Survey).filter(Survey.id == survey_id).first()
        if not survey:
            abort(404, message='Survey {} does not exist'.format(survey_id))
        return survey, 200

    def delete(survey_id):
        survey = session.query(Survey).filter(Survey.id == survey_id).first()
        if not survey:
            abort(404, message='Survey {} does not exist'.format(survey_id))
        delete(survey)
        try:
            session.commit()
        except:
            session.rollback()
        return {}, 204

    @marshal_with(survey_fields)
    def put(self, survey_id):
        survey = session.query(Survey).filter(Survey.id == survey_id).first()
        json_data = request.get_json(format=True)
        survey = Survey(
            survey_name=json_data["survey_name"],
            type=json_data['type'],
            description=json_data["description"],
            event_id=json_data["event_id"]
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
        return survey, 200

    # @marshal_with(user_fields)
    def post(self):
        json_data = request.get_json(force=True)
        survey = Survey(
            survey_name=json_data["survey_name"],
            type=json_data['type'],
            description=json_data["description"],
            event_id=json_data["event_id"]
        )
        session.add(survey)
        try:
            session.commit()
        except:
            session.rollback()
        return 200
