from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_user, login_required, logout_user, current_user #############

from ..extensions import db
from ..models import Server, ServerForm, SearchForm

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
    return render_template('pages/newserver.html.j2', title="Server", current_user=current_user, server=form, new=True)



@app.route('/server/edit/<string:name>', methods=['GET', 'POST'])
@login_required
def edit(name):
    server = Server.query.get(name)
    server_form=ServerForm(obj=server)
    if request.method == 'POST':
        server.name = request.form['name']
        server.image = request.form['image']
        server.description = request.form['description']
        server.starting_cmd = request.form['starting_cmd']
        server.stop_cmd = request.form['stop_cmd']
        server.status_cmd = request.form['status_cmd']
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('pages/newserver.html.j2', title="Server", current_user=current_user, server=server_form, new=False)

@app.route('/server/remove/<string:name>', methods=['GET', 'POST'])
@login_required
def remove(name):
    Server.query.filter(Server.name == name).delete()
    db.session.commit()
    return redirect(url_for('main.dashboard'))
