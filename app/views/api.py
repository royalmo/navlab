# This file is used to serve Apache-Cordova's font-end.

from flask import Blueprint, jsonify, request, make_response
from flask_login import login_user, logout_user, current_user
from flask_babel import gettext, get_locale

from ..extensions import db, bcrypt, auth_header_required, login_manager
from ..models import User, Server

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
