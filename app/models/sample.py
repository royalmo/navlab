from ..extensions import db

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monitor_key = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Integer, nullable=False)
