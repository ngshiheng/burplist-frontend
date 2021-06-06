import logging
from datetime import datetime, timedelta
from functools import lru_cache
from typing import List

from pywebio.input import TEXT, input
from pywebio.output import clear, put_html, put_loading, put_markdown, put_table, put_text, style, use_scope
from pywebio.platform import seo
from pywebio.session import run_js, set_env
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from src.utils.constants import footer, google_adsense, header, landing_page_description, landing_page_gif, landing_page_heading, product_not_found_gif
from src.utils.models import Product, db_connect
from src.utils.validators import validate_search_length

logger = logging.getLogger(__name__)

engine = db_connect()
session = sessionmaker(bind=engine)()


@lru_cache()
def get_product_based_on_query(search: str) -> List[Product]:
    return session.query(Product) \
        .filter(
        or_(
            Product.brand.match(f"'{search}'"),
            Product.style.match(f"'{search}'"),
            Product.name.match(f"'{search}'"),
        ),
        and_(Product.updated_on >= datetime.utcnow() - timedelta(weeks=1)))  \
        .order_by(Product.price_per_quantity) \
        .limit(50) \
        .all()


@seo('Burplist', 'Craft beer prices at your fingertips.')
def index() -> None:
    set_env(auto_scroll_bottom=False)

    # JavaScript stuffs
    run_js(header)
    run_js(google_adsense)
    run_js(footer)

    # Page heading
    put_html(landing_page_heading)
    with use_scope('introduction'):
        put_html(landing_page_gif)
        put_markdown(landing_page_description, lstrip=True)

    while True:
        search = input(
            type=TEXT,
            required=True,
            label='🤩 Start looking here:',
            placeholder='Search for a beer brand, style, or name...',
            help_text='Try: "Little Creatures", "IPA", or "Brewlander Love Wild IPA" ✌️',
            validate=validate_search_length,
        )
        clear('result')
        clear('introduction')

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
            products = []
            try:
                products = get_product_based_on_query(str(search))
                logger.info(get_product_based_on_query.cache_info())

            except Exception as error:
                logger.exception(error)

            finally:
                session.close()

            with use_scope('result'):
                if not products:
                    put_html(product_not_found_gif)
                    put_html(f'<h2 align="center">😢 Oh no, we couldn\'t find anything relevant to "{search}"...</h2>')
                    continue

                put_html(f"""
                <h2 align="center">🔍 Found {len(products)} results for "{search}"...</h2>
                """)
                # Display the final result in a table
                put_table(
                    tdata=[
                        [
                            put_html(f'🍺 <a href="{product.url}" target="_blank">{product.name}</a>'),
                            product.style if product.style else '😬',
                            f'{product.last_price:.2f}',
                            product.quantity,
                            style(put_text(f'{product.price_per_quantity:.2f}'), 'color:red'),
                        ] for product in products
                    ],
                    header=[
                        'Name',
                        'Style',
                        'Price\n($SGD)',
                        'Qty.',
                        'Price/Qty.\n($SGD)',
                    ],
                )
