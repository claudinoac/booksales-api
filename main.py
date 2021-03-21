from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from settings.development import SETTINGS, DATABASE
from urls import routes

define('port', default=9090, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    app = Application(
        routes,
        db=DATABASE,
        **SETTINGS
    )
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
