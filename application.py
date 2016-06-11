from flask import Flask,request,session,jsonify,url_for,render_template,redirect
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.database_module.db import base_session
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            confirm_login, fresh_login_required)
from flask_bcrypt import Bcrypt
from flask_wtf import Form, validators
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_security import login_required
from flask_restful import Api
from settings import DB_URI
from app.database_module.models import User
from flask_oauthlib.client import OAuth
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from resources import UserResource, UserListResource, EventResource, \
    EventListResource, SurveyResource, SurveyListResource

CLIENT_ID = 'GbRmKgbSMmlE2NlugMeFfQIba8hoVyBFsWS8Igsq'
CLIENT_SECRET = 'BfP7jsN8dSsXjGLfTTPiEvarMJOpkZQ2Y7IVVee8X929LfolMV'

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
oauth = OAuth(app)
bcrypt = Bcrypt(app)
heroku = Heroku(app)
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)

remote = oauth.remote_app(
    'remote',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'email'},
    base_url='http://127.0.0.1:5000/api/',
    request_token_url=None,
    access_token_url='http://127.0.0.1:5000/oauth/token',
    authorize_url='http://127.0.0.1:5000/oauth/authorize')

api.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(EventResource, '/event/<int:id>', endpoint='event')
api.add_resource(EventListResource, '/events', endpoint='events')
api.add_resource(SurveyResource, '/survey/<int:id>', endpoint='survey')
api.add_resource(SurveyListResource, '/surveys', endpoint='surveys')

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate_on_submit(self):
        rv = Form.validate_on_submit(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

@app.route('/')
def index():
    if 'remote_oauth' in session:
        resp = remote.get('me')
        return jsonify(resp.data)
    next_url = request.args.get('next') or request.referrer or None
    return remote.authorize(
        callback=url_for('authorized', next=next_url, _external=True)
    )

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
    by processing the form."""
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.get(form.username.data)
    #     if user:
    #         if bcrypt.check_password_hash(user.password, form.password.data):
    #             user.authenticated = True
    #             login_user(user, remember=True)
    #             return redirect(url_for("app.secret"))
    # return 500

    json_data = request.get_json(force=True)
    password = json_data['password']
    user = base_session.query(User).filter_by(username=json_data['username']).first()
    if user:
        if user.check_password(password):
            user.authenticated = True
            login_user(user,remember=True)
            response = "diu"
            return response, 200
        else:
            return 400
    else:
        return 400

@app.route("/secret")
@fresh_login_required
def secret():
    return render_template("secret.html")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    try:
        user.authenticated = False
        logout_user()
    except UnmappedInstanceError:
        pass
    return render_template("logout.html")

@app.route('/authorized')
def authorized():
    resp = remote.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    print(resp)
    session['remote_oauth'] = (resp['access_token'], '')
    return jsonify(oauth_token=resp['access_token'])

@remote.tokengetter
def get_oauth_token():
    return session.get('remote_oauth')

if __name__ == '__main__':
    app.run(debug=True)
