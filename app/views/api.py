# This file is used to serve Apache-Cordova's font-end.

from flask import Blueprint, jsonify, request, make_response
from datetime import datetime
from requests import put

from ..extensions import db, auth_header_required
from ..extensions.login_manager import load_user_from_auth_header
from ..models import Server, FirebaseToken, ServerHistory

app = Blueprint('api', __name__)

@app.route('/servers')
@auth_header_required
def servers():
    response = [
        {
            "id" : server.id,
            "name" : server.name,
            "image_url" : server.image,
            "status" : server.status
        }
        for server in Server.query.all()
    ]
    return make_response(jsonify({'data' : response, 'admin' : load_user_from_auth_header().admin}), 200)

@app.route('/register_token', methods=['POST'])
@auth_header_required
def register_token():
    data = request.get_json()
    token = data.get('token')

    ft = FirebaseToken(user_id=load_user_from_auth_header().id, token=token)

    db.session.add(ft)
    db.session.commit()

    return make_response('OK', 200)

@app.route('/server/<int:id>/start', methods=['GET', 'POST'])
@auth_header_required
def start(id):
    current_user = load_user_from_auth_header()
    if not current_user.admin:
        return make_response('Forbidden', 403)

    server = Server.query.get_or_404(id)
    server.status = True

    if server.endpoint_url is not None:
        key = server.endpoint_url.split('/')[-1]
        put(server.endpoint_url, json={key : 1})

    sh = ServerHistory(server_id=server.id, user_id=current_user.id, timestamp=datetime.now(),active=True)
    db.session.add(sh)
    db.session.commit()
    return make_response("Server started", 204)

@app.route('/server/<int:id>/stop', methods=['GET', 'POST'])
@auth_header_required
def stop(id):
    current_user = load_user_from_auth_header()
    if not current_user.admin:
        return make_response('Forbidden', 403)

    server = Server.query.get_or_404(id)
    server.status = False

    if server.endpoint_url is not None:
        key = server.endpoint_url.split('/')[-1]
        put(server.endpoint_url, json={key : 0})

    sh = ServerHistory(server_id=server.id, user_id=current_user.id, timestamp=datetime.now(),active=False)
    db.session.add(sh)
    db.session.commit()
    return make_response("Server stopped", 204)

@app.route('/server/raw')
@auth_header_required
def raw_data():
    Server.update_status()

    servers = Server.query.all()
    data = [{'id' : server.id, 'status' : server.status} for server in servers]

    return jsonify(data)
