from ..extensions import db
from .sample import Sample

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    # The units of that monitor (Temperature (K), ...)
    label = db.Column(db.String(80), nullable=False)
    # The minimum and maximum value that should be displayed on the graph.
    min_value = db.Column(db.Float, nullable=True)
    max_value = db.Column(db.Float, nullable=True)

def get_monitor_data():
    monitors = Monitor.query.all()
    data = []
    for monitor in monitors:
        samples = Sample.query.filter_by(monitor_key=monitor.key).order_by(Sample.date.desc()).limit(100).all()

        x_axis = [sample.date.strftime('%Y-%m-%d %H:%M:%S') for sample in samples]
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
                'time' : samples[0].date.strftime('%Y-%m-%d %H:%M:%S') if len(samples) > 0 else '---',
                'value' : y_axis[0] if len(y_axis) > 0 else '---'
            }
        })
    
    return data
