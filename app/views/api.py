# This file is used to serve Apache-Cordova's font-end.

from flask import Blueprint, jsonify, request, make_response
from datetime import datetime
from requests import put

from ..extensions import db, auth_header_required
from ..extensions.login_manager import load_user_from_auth_header
from ..models import Server, FirebaseToken, ServerHistory
from ..models.monitor import get_monitor_data

app = Blueprint('api', __name__)

########################

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

@app.route('/monitoring')
@auth_header_required
def monitors():
    return make_response(jsonify({'data' : get_monitor_data(), 'admin' : load_user_from_auth_header().admin}), 200)

########################

@app.route('/register_token', methods=['POST'])
@auth_header_required
def register_token():
    current_user = load_user_from_auth_header()
    data = request.get_json()
    token = data.get('token')

    FirebaseToken.register_token(current_user, token)

    return make_response('OK', 200)

@app.route('/unregister_token', methods=['POST'])
@auth_header_required
def unregister_token():
    current_user = load_user_from_auth_header()
    data = request.get_json()
    token = data.get('token')

    FirebaseToken.unregister_token(current_user, token)

    return make_response('OK', 200)

########################

@app.route('/server/<int:id>/start', methods=['GET', 'POST'])
@auth_header_required
def start(id):
    current_user = load_user_from_auth_header()
    if not current_user.admin:
        return make_response('Forbidden', 403)

    Server.query.get_or_404(id).start(current_user)
    return make_response("Server started", 204)

@app.route('/server/<int:id>/stop', methods=['GET', 'POST'])
@auth_header_required
def stop(id):
    current_user = load_user_from_auth_header()
    if not current_user.admin:
        return make_response('Forbidden', 403)

    Server.query.get_or_404(id).stop(current_user)
    return make_response("Server stopped", 204)
