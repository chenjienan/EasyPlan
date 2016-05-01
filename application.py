from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from settings import DB_URI
from resources import UserResource, UserListResource,EventResource,EventListResource,SurveyResource,SurveyListResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)
api = Api(app)


api.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(EventResource,'/event/<int:id>', endpoint = 'event')
api.add_resource(EventListResource,'/events',endpoint = 'events')
api.add_resource(SurveyResource,'/survey/<int:id>', endpoint = 'survey')
api.add_resource(SurveyListResource,'/surveys',endpoint = 'surveys')
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True)