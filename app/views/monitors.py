from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user
from flask_babel import gettext

from ..extensions import db, login_required, admin_required
from ..models import Monitor, Sample, MonitorForm

from jinja2 import utils
import validators

app = Blueprint('monitors', __name__)

@app.route('/monitoring')
@login_required
def monitoring():
    monitors = Monitor.query.all()
    data = []
    for monitor in monitors:
        samples = Sample.query.filter_by(monitor_key=monitor.key).order_by(Sample.date.desc()).limit(100).all()

        x_axis = [sample.date.timestamp() for sample in samples]
        y_axis = [sample.value for sample in samples]

        # Reversing axis because we want time to be from past to future
        data.append({
            'id' : monitor.id,
            'title' : monitor.title,
            'key' : monitor.key,
            'x_axis' : x_axis[::-1],
            'y_axis' : y_axis[::-1],
            'label' : monitor.label,
            'min_value' : monitor.min_value if monitor.min_value is not None else 'undefined',
            'max_value' : monitor.max_value if monitor.max_value is not None else 'undefined',
            'last_sample' : {
                'time' : samples[0].date.strftime('%Y-%m-%d %H:%M:%S'),
                'value' : y_axis[0]
            }
        })

    return render_template('pages/monitoring.html.j2',
                           title=gettext("Monitoring"),
                           current_user=current_user,
                           navbar_highlight_monitoring=True,
                           monitors=data)

@app.route('/monitor/new', methods=['GET', 'POST'])
@login_required
def new():
    form = MonitorForm()
    
    if form.is_submitted():
        new_monitor = Monitor()
        for key, val in form.data.items():
            if key in ['submit', 'csrf_token']: continue

            if key == 'endpoint_url' or key == 'image':
                if validators.url(val): setattr(new_monitor, key, val)
                continue
            if (str(utils.escape(val)) == val): 
                setattr(new_monitor, key, val)
        
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
                if (str(utils.escape(val)) == val): 
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
