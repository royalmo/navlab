from ..extensions import db

class Mostres(db.Model):
    sensor_name = db.Column(db.String(80), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    value = db.Column(db.Integer, nullable=False)