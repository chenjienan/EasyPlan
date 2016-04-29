from app.database_module.models import User
from app.database_module.db import session
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask import request

user_fields = {
    'username': fields.String,
    'password': fields.String,
    'email': fields.String
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
        session.commit()
        return {}, 204

    @marshal_with(user_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        user = session.query(User).filter(User.id == id).first()
        user.username = parsed_args['username']
        session.add(user)
        session.commit()
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
        session.commit()
        return 200
