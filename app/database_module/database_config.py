from application import db
from app.database_module.models import User, Event, Survey

def create_table():
    db.create_all()