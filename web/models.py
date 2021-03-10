from . import db
from sqlalchemy.sql import func


class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    email = db.Column(db.String(10000))
    comments = db.Column(db.String(10000))
