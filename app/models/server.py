from ..extensions import db

class Server(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    image = db.Column(db.String(80))
    description = db.Column(db.String(80))
    starting_cmd = db.Column(db.String(80), nullable=False)
    stop_cmd = db.Column(db.String(80), nullable=False)
    status_cmd = db.Column(db.String(80), nullable=False)
