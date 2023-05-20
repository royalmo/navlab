from ..extensions import db

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
