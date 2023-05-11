from flask_login import LoginManager, current_user, login_required, logout_user
from functools import wraps
from flask import redirect, url_for, abort
from ..models import User

login_manager = LoginManager()
login_manager.login_view = 'main.users.login'

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
            return redirect(url_for('main.users.login'))
    return wrapper

def admin_login_required(func):
    @wraps(func)
    @active_login_required
    def wrapper(*args, **kwargs):
        if current_user.admin:
            return func(*args, **kwargs)
        else:
            abort(403)
    return wrapper
