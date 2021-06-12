import logging

from pywebio.input import TEXT, input
from pywebio.output import clear, put_html, put_loading, put_markdown, put_table, put_text, style, use_scope
from pywebio.platform import seo
from pywebio.session import run_js, set_env

from src.contents.index import download_description, footer, header, landing_page_description, landing_page_gif, landing_page_heading, no_results
from src.contents.scripts import amplitude_tracking, google_adsense, google_analytics
from src.settings import SEO_DESCRIPTION, SEO_TITLE
from src.utils.search import get_product_based_on_query, get_random_beer, get_random_beer_brand, get_random_beer_style
from src.utils.validators import validate_search_length

logger = logging.getLogger(__name__)


@seo(SEO_TITLE, SEO_DESCRIPTION)
def index() -> None:
    set_env(auto_scroll_bottom=False)

    # JavaScript stuffs
    run_js(header)
    run_js(amplitude_tracking)
    run_js(google_adsense)
    run_js(google_analytics)
    run_js(footer)

    # Page heading
    put_html(landing_page_heading)
    with use_scope('introduction'):
        put_html(landing_page_gif)
        put_markdown(landing_page_description, lstrip=True)
        put_markdown(download_description, lstrip=True)

    while True:
        suggested_brand = get_random_beer_brand()
        suggested_style = get_random_beer_style()
        suggested_beer = get_random_beer()

        help_text = f'Try: "{suggested_brand}", or "{suggested_style}", or "{suggested_beer}" ✌️'

        search = input(
            type=TEXT,
            required=True,
            label='🤩 Start looking here:',
            placeholder='Search for a beer brand, style, or name...',
            help_text=help_text,
            validate=validate_search_length,
        )
        clear('result')
        clear('introduction')
        run_js(f"amplitude.getInstance().logEvent('Keyword searched: \"{search}\"');")

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
            products = get_product_based_on_query(str(search).lower())

            with use_scope('result'):
                if not products:
                    put_html(no_results)
                    put_html(f'<h2 align="center">😢 Oh no, we couldn\'t find anything related to "{search}"...</h2>')
                    put_html('<h6 align="center">Tip: I am not very good with spelling. Can you try again with a different spelling? 😵‍💫</h6>')
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
