# This file is used to serve Apache-Cordova's font-end.

from flask import Blueprint, jsonify, request, make_response
from flask_login import login_user, logout_user, current_user
from flask_babel import gettext, get_locale

from ..extensions import db, bcrypt, login_required, admin_required, login_manager
from ..models import User, Server

app = Blueprint('api', __name__)


@app.route('/login', methods=['POST'])
def login():
    # If user is already logged in
    if current_user.is_authenticated:
        return make_response("Already logged in!", 409)
    
    mail = request.args.get('mail')
    pwd  = request.args.get('password')

    user = User.query.filter_by(email=mail).first()
    if user and bcrypt.check_password_hash(user.password, pwd) and user.active:
        login_user(user, remember=True)
        return make_response("", 204)
    
    return make_response("Unauthorized", 401)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return make_response("", 204)

@app.route('/servers')
@login_required
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
