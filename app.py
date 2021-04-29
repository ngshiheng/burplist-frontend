import argparse

import tornado.httpserver
import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler

from src.index import index
from src.privacy import privacy
from src.terms import terms


class FourOhFourHandler(tornado.web.RequestHandler):
    def get(self, slug):
        self.render('src/templates/404.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080)
    parser.add_argument('-d', '--debug', type=bool, default=False)
    args = parser.parse_args()

    settings = dict(
        site_title='Burplist',
        debug=args.debug,
        host='burplist-frontend.herokuapp.com',
    )

    application = tornado.web.Application([
        (r'/', webio_handler(index)),
        (r'/terms', webio_handler(terms)),
        (r'/privacy', webio_handler(privacy)),
        (r'/([^/]+)', FourOhFourHandler),

    ], **settings)

    application.listen(args.port)
    tornado.ioloop.IOLoop.current().start()
