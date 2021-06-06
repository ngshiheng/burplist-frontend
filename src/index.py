from datetime import datetime, timedelta

from pywebio.input import TEXT, input
from pywebio.output import clear, put_html, put_loading, put_markdown, put_table, put_text, style, use_scope
from pywebio.platform import seo
from pywebio.session import run_js, set_env
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from src.utils.constants import icon_url, mail_to
from src.utils.models import Product, db_connect
from src.utils.validators import validate_search_length

engine = db_connect()
session = sessionmaker(bind=engine)()


@seo('Burplist', 'Craft beer prices at your fingertips')
def index() -> None:
    set_env(auto_scroll_bottom=False)

    # Update favicon
    run_js(f"""
    $('#favicon32,#favicon16').remove();
    $('head').append('<link rel="icon" type="image/x-icon" href="{icon_url}">')
    """)

    # Update footer
    run_js(f"""
    $('footer').html('📬 <a href="mailto:{mail_to}">Contact Us</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
    """)

    # Page title
    put_html(r"""
    <h1 align="center"><strong>Burplist</strong></h1>
    """)
    with use_scope('introduction'):
        put_html(r"""
        <style>
        .img {
            width: auto;
            height: auto;
            max-width: 250;
            max-height: 280px;
            border:2px solid #fff;
            -moz-box-shadow: 10px 10px 5px #ccc;
            -webkit-box-shadow: 10px 10px 5px #ccc;
            box-shadow: 10px 10px 5px #ccc;
            -moz-border-radius:25px;
            -webkit-border-radius:25px;
            border-radius:25px;
        }
        </style>

        <p align="center">
            <img class="img" width="50%" height="50%" src="https://media.giphy.com/media/l3c5RJr6yRKyyIw00/giphy.gif">
        </p>
        """)

        put_markdown(r"""
        # What is this?
        🇸🇬 A collection of **craft beer** prices in Singapore at your finger tips.
        🔎 Think of it as a **search engine** for craft beers in Singapore.

        # What is craft beer?
        🤤 To simply put, craft beers are the more **delicious** alternative to your mainstream beers.
        🍻 In terms of styles, flavours and aroma, craft beers are usually more **diverse** in these aspects.
        💁‍♂️ Craft beers are usually brewed in smaller quantities by passionate brewers who care more about **quality** than quantity.

        # How to use?
        ✍️ Simply enter any beer _brand_, _style_, or _name_ that you want in the search bar and hit "Submit".
        🤑 Prices are ordered starting **from the lowest** to highest.
        """, lstrip=True)

    while True:
        search = input(
            type=TEXT,
            required=True,
            label='🤩 Start looking here:',
            placeholder='Search for a beer brand, style, or name...',
            help_text='Try: "BrewDog", "IPA", or "Hitachino Nest White Ale" ✌️',
            validate=validate_search_length,
        )
        clear('result')
        clear('introduction')

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
            try:
                products = session.query(Product) \
                    .filter(
                        or_(
                            Product.brand.match(f"'{search}'"),
                            Product.style.match(f"'{search}'"),
                            Product.name.match(f"'{search}'"),
                        ),
                        and_(Product.updated_on >= datetime.utcnow() - timedelta(weeks=1)))  \
                    .order_by(Product.price_per_quantity) \
                    .all()

            finally:
                session.close()

            with use_scope('result'):
                if not products:
                    put_html(r"""
                     <style>
                    .img {
                        width: auto;
                        height: auto;
                        max-width: 250;
                        max-height: 280px;
                        border:2px solid #fff;
                        -moz-box-shadow: 10px 10px 5px #ccc;
                        -webkit-box-shadow: 10px 10px 5px #ccc;
                        box-shadow: 10px 10px 5px #ccc;
                        -moz-border-radius:25px;
                        -webkit-border-radius:25px;
                        border-radius:25px;
                    }
                    </style>
                    <p align="center">
                        <img class="img" width="50%" height="50%" src="https://media.giphy.com/media/BEob5qwFkSJ7G/giphy.gif">
                    </p>""")
                    put_html(f'<h2 align="center">😢 Oh no, we couldn\'t find anything relevant to "{search}"...</h2>')
                    continue

                put_html(f"""
                <h2 align="center">🔍 Here are your results for "{search}"...</h2>
                """)
                # Display the final result in a table
                put_table(
                    tdata=[
                        [
                            put_html(f'<a href="{product.url}" target="_blank">🍺 {product.name}</a>'),
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
