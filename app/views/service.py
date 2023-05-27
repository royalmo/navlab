from flask import Blueprint,make_response, send_from_directory, url_for

app = Blueprint('service', __name__)

@app.route('/serviceworker.js')
def service_worker():
    response = make_response(send_from_directory('static/js/','serviceworker.js'))
    response.headers['Content-Type'] = 'application/javascript'
    response.headers['Service-Worker-Allowed'] = '/'
    return response
