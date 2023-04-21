from flask import Flask
from .extensions import db, bcrypt, login_manager
from .views import app as main

app = Flask(__name__)

app.config.from_pyfile('settings/development.py')

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

app.register_blueprint(main, url_prefix='')

if __name__ == "__main__":
    app.run()
