from flask import request, make_response
from flask_login import LoginManager, current_user, login_required, logout_user
from functools import wraps
from flask import redirect, url_for, abort
from ..models import User
from .bcrypt import bcrypt

login_manager = LoginManager()
login_manager.login_view = 'main.users.login'

def unauthorized_callback():
    if request.path.startswith('/api'):
        return make_response('Unauthorized', 401)
    
    return redirect(url_for(login_manager.login_view, next=request.full_path))

login_manager.unauthorized_handler(unauthorized_callback)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def active_login_required(func):
    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.active:
            return func(*args, **kwargs)
        else:
            logout_user()
            return login_manager.unauthorized()
    return wrapper

def admin_login_required(func):
    @wraps(func)
    @active_login_required
    def wrapper(*args, **kwargs):
        if current_user.admin:
            return func(*args, **kwargs)
        else:
            return make_response('Forbidden', 403)
    return wrapper

def load_user_from_auth_header():
    return User.query.filter_by(email=request.authorization.username).first()

def auth_header_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return make_response('Unauthorized', 401)

        user = load_user_from_auth_header()
        if not bcrypt.check_password_hash(user.password, auth.password):
            return make_response('Unauthorized', 401)

        return func(*args, **kwargs)
    return wrapper
