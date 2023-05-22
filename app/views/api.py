# This file is used to serve Apache-Cordova's font-end.

from flask import Blueprint, jsonify, request, make_response
from flask_login import login_user, logout_user, current_user
from flask_babel import gettext, get_locale

from ..extensions import db, auth_header_required
from ..extensions.login_manager import load_user_from_auth_header
from ..models import User, Server, FirebaseToken

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
    return make_response(jsonify(response), 200)

@app.route('/register_token')
@auth_header_required
def register_token():
    data = request.get_json()
    token = data.get('token')

    ft = FirebaseToken(user_id=load_user_from_auth_header().id, token=token)

    db.session.add(ft)
    db.session.commit()

    return make_response('OK', 200)
