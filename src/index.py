from pywebio.input import TEXT, input
from pywebio.output import clear, put_html, put_loading, put_markdown, put_table, put_text, style, use_scope
from pywebio.platform import seo
from pywebio.session import run_js, set_env
from sqlalchemy.orm import sessionmaker

from src.utils.models import Product, db_connect
from src.utils.validators import validate_search_length

engine = db_connect()
session = sessionmaker(bind=engine)()


@seo('Burplist', 'Beer prices at your fingertips')
def index() -> None:
    set_env(auto_scroll_bottom=False)
    run_js("""
    $('footer').html('📬 <a href="mailto:jerry@burplist.me">Contact Us</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
    """)
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
        🇸🇬 A collection of craft beer prices in Singapore.
        🖐 Prices of **all** beers in Singapore at your fingertips.

        # What is craft beer?
        🤤 To simply put, craft beers are the more **delicious** alternative to your mainstream beers.
        🍻 In terms of styles, flavours and aroma, craft beers are usually more **diverse** in these aspects.
        💁‍♂️ Craft beers are usually brewed in smaller quantities by passionate brewers who care more about **quality** than quantity.
        """, lstrip=True)

    while True:
        search = input(
            type=TEXT,
            required=True,
            label='🤩 Start looking here:',
            placeholder='Search for a beer name...',
            help_text='Try: "Hitachino Nest White Ale"',
            validate=validate_search_length,
        )
        clear('introduction')
        clear('result')

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
            products = session.query(Product) \
                .filter(Product.name.match(f"'{search}'")) \
                .order_by(Product.price_per_quantity.asc()) \
                .all()
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
                            put_html(f'<a href="{product.url}" target="_blank">{product.name}</a>'),
                            f'{product.last_price:.2f}',
                            product.quantity,
                            style(put_text(f'{product.price_per_quantity:.2f}'), 'color:red'),
                        ] for product in products
                    ],
                    header=[
                        'Name',
                        'Price ($SGD)',
                        'Qty.',
                        'Price/Qty. ($SGD)',
                    ],
                )
