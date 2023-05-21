from ..extensions import db

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    # The units of that monitor (Temperature (K), ...)
    label = db.Column(db.String(80), nullable=False)
    # The minimum and maximum value that should be displayed on the graph.
    min_value = db.Column(db.Integer, nullable=True)
    max_value = db.Column(db.Integer, nullable=True)
