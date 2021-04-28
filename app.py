import argparse

import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler

from src.index import index
from src.terms import terms

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080)
    args = parser.parse_args()

    application = tornado.web.Application([
        (r'/', webio_handler(index)),
        (r'/terms', webio_handler(terms)),
    ])

    application.listen(port=args.port)
    tornado.ioloop.IOLoop.current().start()
