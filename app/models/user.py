from ..extensions import db, bcrypt
from flask_login import UserMixin
from babel import Locale

from jinja2 import utils

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
    
    def update_with_form(self, form, admin=False):
        user = self
        if (str(utils.escape(form.name.data)) == form.name.data):
            user.name = form.name.data
        if (str(utils.escape(form.email.data)) == form.email.data):
            user.email = form.email.data
        user.lang=str(utils.escape(form.language.data))
        if form.password.data and form.password.data==form.password_confirm.data:
            user.password = bcrypt.generate_password_hash(form.password.data)
        user.admin = ((not admin) and user.admin) or (admin and form.admin.data)
        user.active = ((not admin) and user.active) or (admin and form.active.data)
        db.session.commit()
