from ..extensions import db

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image = db.Column(db.String(80))
    description = db.Column(db.String(80))
    starting_cmd = db.Column(db.String(80), nullable=False)
    stop_cmd = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean)
