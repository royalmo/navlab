from ..extensions import db
from datetime import datetime
from .user import User

class FirebaseToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def get_user(self):
        return User.query.get(self.user_id)
