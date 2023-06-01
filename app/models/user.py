from ..extensions import db, bcrypt, firebase
from flask_login import UserMixin
from babel import Locale
from .firebase_token import FirebaseToken

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
        user.name = form.name.data
        user.email = form.email.data
        user.lang=form.language.data
        if form.password.data and form.password.data==form.password_confirm.data:
            user.password = bcrypt.generate_password_hash(form.password.data)
        user.admin = ((not admin) and user.admin) or (admin and form.admin.data)
        user.active = ((not admin) and user.active) or (admin and form.active.data)
        db.session.commit()
    
    @classmethod
    def send_to_admins(model, title, message):
        fts = FirebaseToken.query.join(FirebaseToken, FirebaseToken.user_id == model.id).filter(model.admin == True).all()
        if len(fts) == 0: return

        server_token = firebase.get_bearer_token()
        for ft in fts:
            client_token = ft.token
            r = firebase.send_notification(title, message, client_token, server_token)
            if not r: # Failed to deliver notification, remove FT.
                db.session.delete(ft)

        db.session.commit()

    @classmethod
    def notify_new_user(model, new_user):
        model.send_to_admins("New User", f"User {new_user.name} just landed, activate their account!")

    @classmethod
    def notify_server_started(model, server, user):
        model.send_to_admins("Server started", f"Server {server.name} been just started by {user.name}.")

    @classmethod
    def notify_server_stopped(model, server, user):
        model.send_to_admins("Server stopped", f"Server {server.name} been just stopped by {user.name}.")
