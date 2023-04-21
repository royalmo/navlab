from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user

from .users import app as users_view

app = Blueprint('main', __name__)
app.register_blueprint(users_view, url_prefix='')

@app.route('/')
def index():
    return redirect(url_for('.dashboard'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/dashboard.html.j2', title="Dashboard", current_user=current_user)
