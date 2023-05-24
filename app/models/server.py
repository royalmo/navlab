from ..extensions import db
from .sample import Sample

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image = db.Column(db.String(80))
    description = db.Column(db.String(80))
    endpoint_url = db.Column(db.String(80))
    status = db.Column(db.Boolean)

    @classmethod
    def update_status(model):
        for srv in model.query.all():
            if srv.endpoint_url is None: continue
            # Bypassing debug or demo devices
            if "ngrok-free.app" in srv.endpoint_url: continue
            
            key = srv.endpoint_url.split('/')[-1]
            smp = Sample.query.filter_by(monitor_key=key).order_by(Sample.date.desc()).first()
            if smp:
                srv.status = bool(smp.value)

        db.session.commit()
