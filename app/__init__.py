from flask import Flask, render_template, request, send_from_directory
from flask_login import current_user
from .extensions import db, bcrypt, login_manager, babel, cors
from .extensions.babel import get_locales
from .views import app as main
from .settings import is_production
import os

app = Flask(__name__)

app.config.from_pyfile('settings/production.py' if is_production() else 'settings/development.py')

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
babel.init_app(app)
cors.init_app(app)

app.register_blueprint(main, url_prefix='')

@babel.localeselector
def get_locale():
    available_langs = [ x[0] for x in get_locales() ]
    lang = request.args.get('lang')
    if lang and lang in available_langs: return lang
    if current_user.is_authenticated: return current_user.lang
    return request.accept_languages.best_match(available_langs)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html.j2', title='404 Error'), 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()
