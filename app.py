# Main file. See README.md for more details.

from app import app, is_production
from sys import argv

if is_production() or (len(argv) == 2 and argv[1] == '--listen-all'):
    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

else:
    print('Running in development mode!!')
    app.run()
