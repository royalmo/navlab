from flask import Blueprint, render_template
from flask_login import current_user
from flask_babel import gettext

from ..extensions import db, login_required
from ..models import Monitor, Sample

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
            'title' : monitor.title,
            'key' : monitor.key,
            'x_axis' : x_axis[::-1],
            'y_axis' : y_axis[::-1],
            'label' : monitor.label,
            'min_value' : monitor.min_value if monitor.min_value else 'undefined',
            'max_value' : monitor.max_value if monitor.max_value else 'undefined',
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
