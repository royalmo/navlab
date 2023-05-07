# Main file. See README.md for more details.

from app import app
from gevent.pywsgi import WSGIServer

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
