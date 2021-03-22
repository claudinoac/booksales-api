from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application
from settings.base import SETTINGS, DATABASE
from urls import routes


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
