from flask import Flask

from flask import Flask, request, render_template, url_for, redirect, flash
from app.DatabaseModule.models import db,User

import os

app = Flask(__name__)
db.init_app(app)
app.config.from_object('config.DevelopmentConfig')



#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


@app.route('/')
def index():
    # admin =User('123','name','psw1')
    # db.session.add(admin)
    # db.session.commit()
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run(debug=True)