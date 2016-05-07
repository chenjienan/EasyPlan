from application import app, db
from app.database_module.models import User, Event, Survey
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def init_database():
    db.create_all()
    print('Initialized the database')


@manager.command
def drop_database():
    if prompt_bool("Are you sure you want to remove the database"):
        db.drop_all()
        print('Dropped the database')

if __name__ == "__main__":
    manager.run()
