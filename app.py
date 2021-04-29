import argparse

import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler
from tornado.httpserver import HTTPServer

from src.index import index
from src.privacy import privacy
from src.terms import terms

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080)
    parser.add_argument('-d', '--debug', type=bool, default=False)
    args = parser.parse_args()

    application = tornado.web.Application(
        [
            (r'/', webio_handler(index)),
            (r'/terms', webio_handler(terms)),
            (r'/privacy', webio_handler(privacy)),
        ],
        debug=args.debug,
    )

    http_server = HTTPServer(application)
    http_server.listen(port=args.port)
    tornado.ioloop.IOLoop.instance().start()
