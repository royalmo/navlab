from flask import Flask, render_template, url_for
from .extensions import db, bcrypt, login_manager
from .views import app as main

app = Flask(__name__)

app.config.from_pyfile('settings/development.py')

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

app.register_blueprint(main, url_prefix='')

@app.errorhandler(403)
def page_not_found(error):
    return render_template('errors/404.html.j2', title='404 Error'), 404

if __name__ == "__main__":
    app.run()
