from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import current_user
from ..extensions import login_required
from flask_babel import gettext

from .users import app as users_view
from .servers import app as servers_view
from .api import app as api_view
from ..models import Server, SearchForm

app = Blueprint('main', __name__)
app.register_blueprint(api_view, url_prefix='/api')
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
        servers = Server.query.filter(Server.name.contains(search_query)).all()
        search_form.data['search'] = search_query
    else:
        servers = Server.query.all()

    return render_template('pages/dashboard.html.j2',
                           title=gettext("Dashboard"),
                           current_user=current_user,
                           serverlist=servers,
                           search_form=search_form,
                           navbar_highlight_dashboard=True)

@app.route('/monitoring')
@login_required
def monitoring():
    return render_template('pages/monitoring.html.j2',
                           title=gettext("Monitoring"),
                           current_user=current_user,
                           navbar_highlight_monitoring=True)
