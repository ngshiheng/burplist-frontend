import os

import tornado.ioloop
import tornado.options
import tornado.web
from pywebio.platform.tornado import webio_handler as ws_webio_handler
from pywebio.platform.tornado_http import webio_handler as http_webio_handler
from tornado.options import define, options

from src.pages import feedback, index, privacy, terms
from src.settings import ALLOWED_ORIGINS, RECONNECT_TIMEOUT, STATIC

define('port', default=8080, help='Run on the given port', type=int)
define('debug', default=False, help='Run on the debug mode', type=bool)


class FourOhFourHandler(tornado.web.RequestHandler):
    def get(self, slug: str) -> None:
        del slug  # Unused
        self.render('src/templates/404.html')


def main() -> None:
    tornado.options.parse_command_line()

    settings = dict(
        site_title='Burplist',
        debug=options.debug,
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        static_url_prefix=STATIC,
    )

    app = tornado.web.Application(
        [
            (r'/', ws_webio_handler(index, reconnect_timeout=RECONNECT_TIMEOUT, allowed_origins=ALLOWED_ORIGINS)),
            (r'/terms', http_webio_handler(terms)),
            (r'/privacy', http_webio_handler(privacy)),
            (r'/feedback', http_webio_handler(feedback)),
            (r'/([^/]+)', FourOhFourHandler),
        ], **settings
    )

    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
