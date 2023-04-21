# Database initialization, see README.md for more info.
from app import app, db
with app.app_context():
    db.create_all()
