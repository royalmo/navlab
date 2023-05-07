from flask import Flask, render_template, request
from flask_login import current_user
from .extensions import db, bcrypt, login_manager, babel
from .views import app as main

app = Flask(__name__)

app.config.from_pyfile('settings/development.py')

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
babel.init_app(app)

app.register_blueprint(main, url_prefix='')

@babel.localeselector
def get_locale():
    if current_user.is_authenticated: return current_user.lang
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html.j2', title='404 Error'), 404

if __name__ == "__main__":
    app.run()
