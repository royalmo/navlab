from flask import Blueprint, render_template, url_for, redirect, request, make_response
from flask_login import current_user
from flask_babel import gettext

from ..extensions import db, login_required, admin_required
from ..models import Server, ServerForm, SearchForm
from app.models.server_history import ServerHistory
from datetime import datetime

app = Blueprint('servers', __name__)

@app.route('/server/new', methods=['GET', 'POST'])
@login_required
def newserver():
    form = ServerForm()
    
    if (form.is_submitted()):
        new_server = Server(**{key : val for key, val in form.data.items() if key not in ['submit', 'csrf_token']})
        db.session.add(new_server)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('pages/newserver.html.j2', title=gettext("New Server"), current_user=current_user, server=form, new=True)

@app.route('/server/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    server = Server.query.get_or_404(id)
    server_history_list = ServerHistory.query.filter_by(server_id=id).order_by(ServerHistory.timestamp.desc()).limit(10).all()
    server_form=ServerForm(obj=server)
    if request.method == 'POST':
        if current_user.admin: # Only admins can edit
            for key, val in server_form.data.items():
                if key in ['submit', 'csrf_token']: continue
                setattr(server, key, val)
            db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('pages/newserver.html.j2', title=gettext("Edit Server"), current_user=current_user, server=server_form, new=False, id=id, server_history_list=server_history_list)

@app.route('/server/<int:id>/remove', methods=['GET', 'POST'])
@admin_required
def remove(id):
    Server.query.filter(Server.id == id).delete()
    db.session.commit()
    return redirect(url_for('main.dashboard'))

@app.route('/server/<int:id>/start', methods=['GET', 'POST'])
@login_required
def start(id):
    server = Server.query.get_or_404(id)
    server.status = True
    sh = ServerHistory(server_id=server.id, user_id=current_user.name, timestamp=datetime.now(),active=True)
    db.session.add(sh)
    db.session.commit()
    return make_response("Server started", 204)

@app.route('/server/<int:id>/stop', methods=['GET', 'POST'])
@login_required
def stop(id):
    server = Server.query.get_or_404(id)
    server.status = False
    sh = ServerHistory(server_id=server.id, user_id=current_user.name, timestamp=datetime.now(),active=False)
    db.session.add(sh)
    db.session.commit()
    return make_response("Server stopped", 204)
