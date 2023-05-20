from flask import Blueprint, render_template
from flask_login import current_user
from flask_babel import gettext

from ..extensions import db, login_required
from ..models import Monitor, Sample

app = Blueprint('monitors', __name__)

@app.route('/monitoring')
@login_required
def monitoring():
    monitors = [
        {
            'title' : 'Arduino BlaBla',
            'key' : 'led',
            'x_axis' : [1, 2, 5],
            'y_axis' : [1, 1, 0],
            'label' : 'Temperature'
        }
    ]
    return render_template('pages/monitoring.html.j2',
                           title=gettext("Monitoring"),
                           current_user=current_user,
                           navbar_highlight_monitoring=True,
                           monitors=monitors)
