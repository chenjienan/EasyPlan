from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from settings import DB_URI
from resources import UserResource, UserListResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)
api = Api(app)


api.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api.add_resource(UserListResource, '/users', endpoint='users')

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True)