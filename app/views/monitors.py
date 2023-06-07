from flask import Blueprint, render_template, redirect, url_for, jsonify
from flask_login import current_user
from flask_babel import gettext

from ..extensions import db, login_required, admin_required
from ..models import Monitor, MonitorForm
from ..models.monitor import get_monitor_data

app = Blueprint('monitors', __name__)

@app.route('/monitoring')
@login_required
def monitoring():
    data = get_monitor_data()

    return render_template('pages/monitoring.html.j2',
                           title=gettext("Monitoring"),
                           current_user=current_user,
                           navbar_highlight_monitoring=True,
                           monitors=data)

@app.route('/monitoring/raw')
@login_required
def monitoring_raw():
    data = get_monitor_data()

    return jsonify(data)

@app.route('/monitor/new', methods=['GET', 'POST'])
@login_required
def new():
    form = MonitorForm()
    
    if form.is_submitted():
        new_monitor = Monitor(**{key : val for key, val in form.data.items() if key not in ['submit', 'csrf_token']})
        db.session.add(new_monitor)
        db.session.commit()
        return redirect(url_for('main.monitors.monitoring'))
    return render_template('pages/newmonitor.html.j2', title=gettext("New Monitor"), current_user=current_user, monitor=form, new=True)

@app.route('/monitor/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    monitor = Monitor.query.get_or_404(id)
    monitor_form=MonitorForm(obj=monitor)
    if monitor_form.is_submitted():
        if current_user.admin: # Only admins can edit
            for key, val in monitor_form.data.items():
                if key in ['submit', 'csrf_token']: continue
                setattr(monitor, key, val)
            db.session.commit()
        return redirect(url_for('main.monitors.monitoring'))
    return render_template('pages/newmonitor.html.j2', title=gettext("Edit Monitor"), current_user=current_user, monitor=monitor_form, new=False, id=id)

@app.route('/monitor/<int:id>/remove', methods=['GET', 'POST'])
@admin_required
def remove(id):
    Monitor.query.filter(Monitor.id == id).delete()
    db.session.commit()
    return redirect(url_for('main.monitors.monitoring'))
