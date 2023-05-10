from ..extensions import db
from flask_login import UserMixin
from babel import Locale

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    lang = db.Column(db.String(10), nullable=False, default="en")

    def parsed_lang(self):
        return Locale(self.lang).get_display_name().capitalize()
