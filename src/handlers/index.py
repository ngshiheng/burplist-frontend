__all__ = ['index']
import logging
from functools import partial
from typing import Union

from pywebio.input import TEXT, input
from pywebio.io_ctrl import Output, OutputList
from pywebio.output import clear, put_buttons, put_collapse, put_html, put_link, put_loading, put_markdown, put_table, put_text, scroll_to, style, use_scope
from pywebio.platform import seo
from pywebio.platform.page import config
from pywebio.session import run_js, set_env
from src.database.models import Product
from src.database.utils import get_product_based_on_query, get_random_beer, get_random_beer_brand, get_random_beer_style, get_random_results_not_found_gif
from src.settings import SEO_DESCRIPTION, SEO_TITLE
from src.utils.constants import GA_JS_CODE, GA_JS_FILE, POPULAR_BEER_BRANDS, POPULAR_BEER_STYLES
from src.utils.contents.charts import show_price_history_graph_popup
from src.utils.contents.index import DOWNLOAD_DESCRIPTION, FOOTER, HEADER, LANDING_PAGE_DESCRIPTION, LANDING_PAGE_HEADING, LANDING_PAGE_SUBHEADING, LOAD_CSS, PRODUCT_HUNT_FEATURED_BANNER
from src.utils.validators import validate_search_length

logger = logging.getLogger(__name__)


def generate_table_header() -> list[Union[Output, OutputList, str]]:
    return [
        style(put_text('🛍\nPlatform'), 'text-align:center;'),
        style(put_text('🍻\nName'), 'text-align:center;'),
        style(put_text('✨\nStyle'), 'text-align:center;'),
        style(put_text('💲\nPrice'), 'text-align:center;'),
        style(put_text('🛒\nQty.'), 'text-align:center;'),
        style(put_text('💸\nPrice/Qty.'), 'text-align:center;'),
    ]


def generate_table_data(products: list[Product]) -> list[list[Union[Output, OutputList, str]]]:
    return [
        [
            # Platform
            style(put_text(product.platform.title()), 'text-align:center'),
            # Name
            put_collapse(
                product.name, style(
                    [
                        put_table([
                            ['Volume', 'ABV', 'Link', 'Price Chart'],
                            [
                                f'{product.volume}ml' if product.volume else '🙊',
                                f'{product.abv}%' if product.abv else '🙈',
                                put_link(name='View', url=product.url, new_window=True),
                                put_buttons(
                                    [dict(label='Show', value={'id': product.id, 'name': product.name}, color='primary')],
                                    onclick=partial(show_price_history_graph_popup, {'id': product.id, 'name': product.name}),
                                ),
                            ],
                        ]),
                    ], 'text-align:center;',
                ), open=False,
            ),
            # Style
            style(put_text(product.style if product.style else '😬'), 'text-align:center;'),
            # Price
            f'${product.last_price:.2f}',
            # Qty.
            style(put_text(product.quantity), 'text-align:center'),
            # Price/Qty.
            style(
                put_link(name=f'${product.price_per_quantity:.2f}', url=product.url, new_window=True),
                'color:red; font-weight:bold; text-align:center; text-decoration: underline;',
            ),
        ] for product in products
    ]


@seo(SEO_TITLE, SEO_DESCRIPTION)
@config(theme="minty", js_file=GA_JS_FILE, js_code=GA_JS_CODE)
def index() -> None:
    """
    Renders the home page of Burplist
    """
    set_env(auto_scroll_bottom=False)

    # JavaScript stuffs
    run_js(HEADER)
    run_js(FOOTER)
    put_html(LOAD_CSS)

    # Page heading
    put_html(LANDING_PAGE_HEADING)
    with use_scope('introduction'):
        put_html(PRODUCT_HUNT_FEATURED_BANNER)
        put_html(LANDING_PAGE_SUBHEADING)
        put_markdown(LANDING_PAGE_DESCRIPTION, lstrip=True)
        put_markdown(DOWNLOAD_DESCRIPTION, lstrip=True)

    while True:
        suggested_brand = get_random_beer_brand()
        suggested_style = get_random_beer_style()
        suggested_beer = get_random_beer()

        help_text = f'Try: "{suggested_brand}", or "{suggested_style}", or "{suggested_beer}" ✌️'

        search = input(
            type=TEXT,
            required=True,
            label='🤩 Start looking here:',
            placeholder='Search for a platform, beer brand, style, or name...',
            help_text=help_text,
            validate=validate_search_length,
            datalist=POPULAR_BEER_BRANDS + POPULAR_BEER_STYLES,
        )

        clear('result')
        clear('introduction')
        scroll_to(position='top')

        # Amplitude tracking
        run_js(f"amplitude.getInstance().logEvent('Keyword searched: \"{search}\"');")

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
            products = get_product_based_on_query(str(search).lower())

            with use_scope('result'):
                if not products:
                    put_html(get_random_results_not_found_gif())
                    put_html(f'<h2 align="center">😢 Oh no, we couldn\'t find anything related to <i>"{search}"</i>...</h2>')
                    put_html('<h6 align="center">💡 Please try with a different keyword</h6>')
                    continue

                put_html(f"""
                <h2 align="center">🔍 Found {len(products)} results for <i>"{search}"</i>...</h2>
                """)

                # Display the final result in a table
                put_table(
                    tdata=generate_table_data(products),
                    header=generate_table_header(),
                )
