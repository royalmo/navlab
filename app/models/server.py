from ..extensions import db

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image = db.Column(db.String(80))
    description = db.Column(db.String(80))
    endpoint_url = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean)
