from ..extensions import db
from .sample import Sample

from requests import get

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image = db.Column(db.String(80))
    description = db.Column(db.String(80))
    endpoint_url = db.Column(db.String(80))
    status = db.Column(db.Boolean)

    @classmethod
    def update_status(model, all=False):
        for srv in model.query.all():
            if srv.endpoint_url is None: continue

            key = srv.endpoint_url.split('/')[-1]

            if "navlab.ericroy.net" in srv.endpoint_url:
                smp = Sample.query.filter_by(monitor_key=key).order_by(Sample.date.desc()).first()
                if smp:
                    srv.status = bool(smp.value)
            elif all: # Do the request
                try:
                    r = get(srv.endpoint_url)
                    if r.status_code!=200: continue
                    d=r.json()
                    srv.status = bool(int(d[key]))
                except: pass # Ignoring errors

        db.session.commit()
