# Main file. See README.md for more details.

from app import app
from sys import argv

if len(argv) == 2 and argv[1] == '--production':
    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

else:
    app.run()
