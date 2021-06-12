import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pywebio.platform.tornado_http import webio_handler as http_webio_handler
from tornado.options import define, options

from src.index import index
from src.privacy import privacy
from src.settings import ALLOWED_ORIGINS, STATIC
from src.terms import terms

define('port', default=8080, help='Run on the given port', type=int)
define('debug', default=False, help='Run on the debug mode', type=bool)


class FourOhFourHandler(tornado.web.RequestHandler):
    def get(self, slug):
        self.render('src/templates/404.html')


def main():
    tornado.options.parse_command_line()

    settings = dict(
        site_title='Burplist',
        debug=options.debug,
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        static_url_prefix=STATIC,
    )

    app = tornado.web.Application([
        (r'/', http_webio_handler(index, allowed_origins=ALLOWED_ORIGINS)),
        (r'/terms', http_webio_handler(terms)),
        (r'/privacy', http_webio_handler(privacy)),
        (r'/([^/]+)', FourOhFourHandler),
    ], **settings)

    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
