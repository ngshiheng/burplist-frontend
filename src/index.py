import logging
from functools import partial

from pywebio.input import TEXT, input
from pywebio.output import clear, put_buttons, put_collapse, put_html, put_link, put_loading, put_markdown, put_table, put_text, scroll_to, style, use_scope
from pywebio.platform import seo
from pywebio.session import run_js, set_env

from src.contents.graph import show_price_history_graph
from src.contents.index import download_description, footer, header, landing_page_description, landing_page_heading, landing_page_subheading, load_css
from src.contents.scripts import amplitude_tracking, google_analytics
from src.settings import SEO_DESCRIPTION, SEO_TITLE
from src.utils.search import get_product_based_on_query, get_random_beer, get_random_beer_brand, get_random_beer_style, get_random_results_not_found_gif
from src.utils.validators import validate_search_length

logger = logging.getLogger(__name__)


@seo(SEO_TITLE, SEO_DESCRIPTION)
def index() -> None:
    set_env(auto_scroll_bottom=False)

    # JavaScript stuffs
    run_js(header)
    run_js(amplitude_tracking)
    run_js(google_analytics)
    run_js(footer)
    put_html(load_css)

    # Page heading
    put_html(landing_page_heading)
    with use_scope('introduction'):
        put_html(landing_page_subheading)
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
        scroll_to(position='top')
        run_js(f"amplitude.getInstance().logEvent('Keyword searched: \"{search}\"');")

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
            products = get_product_based_on_query(str(search).lower())

            with use_scope('result'):
                if not products:
                    put_html(get_random_results_not_found_gif())
                    put_html(f'<h2 align="center">😢 Oh no, we couldn\'t find anything related to "{search}"...</h2>')
                    put_html('<h6 align="center">💡 I am not very good with spelling. Can you try again with a different spelling?</h6>')
                    continue

                put_html(f"""
                <h2 align="center">🔍 Found {len(products)} results for "{search}"...</h2>
                """)

                # Display the final result in a table
                put_table(
                    tdata=[
                        [
                            style(put_link(name=product.platform.title(), url=product.url, new_window=True), 'text-align:center'),
                            put_collapse(product.name, style([
                                put_table([
                                    ['Volume', 'ABV', 'Link', 'Price Chart'],
                                    [
                                        f'{product.volume}ml' if product.volume else '🙊',
                                        f'{product.abv}%' if product.abv else '🙈',
                                        put_link(name='View', url=product.url, new_window=True),
                                        put_buttons([dict(label='Show', value={'id': product.id, 'name': product.name}, color='primary')], onclick=partial(show_price_history_graph, {'id': product.id, 'name': product.name})),
                                    ],
                                ]),
                            ], 'text-align:center;'), open=False),
                            style(put_text(product.style if product.style else '😬'), 'text-align:center'),
                            f'${product.last_price:.2f}',
                            style(put_text(product.quantity), 'text-align:center'),
                            style(put_link(name=f'${product.price_per_quantity:.2f}', url=product.url, new_window=True), 'color:red; font-weight:bold; text-align:center;'),
                        ] for product in products
                    ],
                    header=[
                        style(put_text('🛍\nPlatform'), 'text-align:center;'),
                        style(put_text('🍻\nName'), 'text-align:center;'),
                        style(put_text('✨\nStyle'), 'text-align:center;'),
                        style(put_text('💲\nPrice'), 'text-align:center;'),
                        style(put_text('🛒\nQty.'), 'text-align:center;'),
                        style(put_text('💸\nPrice/Qty.'), 'text-align:center;'),
                    ],
                )
