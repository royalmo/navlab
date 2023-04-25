from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user

from .users import app as users_view
from .servers import app as servers_view
from ..models import Server, SearchForm

app = Blueprint('main', __name__)
app.register_blueprint(users_view, url_prefix='')
app.register_blueprint(servers_view, url_prefix='')

@app.route('/')
def index():
    return redirect(url_for('.dashboard'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    search_form = SearchForm(request.form)
    search_query = request.args.get('search')
    if request.method == 'GET' and search_query:
        servers = Server.query.filter(Server.name.contains(search_query))
        search_form.data['search'] = search_query
    else:
        servers = Server.query.all()

    return render_template('pages/dashboard.html.j2', title="Dashboard", current_user=current_user, serverlist=servers, search_form=search_form)
