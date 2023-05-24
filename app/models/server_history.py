from ..extensions import db
from datetime import datetime
from .user import User

class ServerHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    active = db.Column(db.Boolean, default=True)

    def get_user(self):
        return User.query.get(self.user_id)

