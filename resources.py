from app.database_module.models import User
from app.database_module.db import session
from flask_restful import Resource, reqparse, abort, fields, marshal_with

user_fields = {
    'username': fields.String,
    'password': fields.String,
    'email': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('user', type=str)


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message='User {} does not exist'.format(id))
        return user
