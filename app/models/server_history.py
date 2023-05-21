from ..extensions import db
from datetime import datetime

class ServerHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    active = db.Column(db.Boolean, default=True)


