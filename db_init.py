# Database initialization, see README.md for more info.
from app import app, db
import sqlite3, os

# Remove the database file if it exists
if os.path.exists('app/navlab.db'):
    os.remove('app/navlab.db')

# Create app tables
with app.app_context():
    db.create_all()

# Connect to the database and populate them
conn = sqlite3.connect('app/navlab.db')

with open('db_seed.sql', 'r') as f:
    sql = f.read()

conn.executescript(sql)
conn.commit()
conn.close()
