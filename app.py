from pywebio import start_server
from pywebio.input import TEXT, input
from pywebio.output import clear, put_html, put_markdown, put_table, put_text, style, use_scope
from pywebio.session import set_env
from sqlalchemy.orm import sessionmaker

from src.models import Product, db_connect


def main():
    # Connects to a database session
    engine = db_connect()
    session = sessionmaker(bind=engine)()

    set_env(title='Burplist', auto_scroll_bottom=True)

    with use_scope('root'):
        put_html(r"""
        <h1 align="center"><strong>Burplist</strong></h1>
        <style>
        .img {
            width: 300;
            height: 300px;
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

    with use_scope('introduction'):
        put_markdown(r"""
        ## What is this?
        A collection of craft beer prices in Singapore 🇸🇬
        The prices of all beers in Singapore at your fingertip 🍺

        ## What is craft beer?
        To simply put, craft beers are the more delicious alternative to mainstream, mass-market beers.
        In terms of flavours and aroma, craft beer is much more diverse
        Craft beer is much more diverse in styles and distinctive in characters, flavours and aroma.
        Craft beers are usually brewed in smaller quantities by passionate brewers who care more about quality than quantity.
        """, lstrip=True)

    while True:
        search = input(
            type=TEXT,
            required=True,
            label='Start looking 🍻',
            placeholder='Search for a beer name...',
            help_text='Try: Hitachino Nest White Ale',
        )
        clear('result')
        clear('introduction')

        # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
        products = session.query(Product) \
            .filter(Product.name.match(f"'{search}'")) \
            .order_by(Product.price_per_quantity.asc()) \
            .all()
        session.close()

        with use_scope('result'):
            if not products:
                put_text('Oh no, we couldn\'t find anything relevant... 😢')
                continue

            # Display the final result in a table
            put_table(
                tdata=[
                    [
                        product.vendor.title(),
                        put_markdown(f'[{product.name}]({product.url})'),
                        f'{product.last_price:.2f}',
                        product.quantity,
                        style(put_text(f'{product.price_per_quantity:.2f}'), 'color:red'),
                    ] for product in products
                ],
                header=[
                    'Vendor',
                    'Name',
                    'Price ($SGD)',
                    'Quantity',
                    'Price/Quantity ($SGD)',
                ],
            )


if __name__ == '__main__':
    start_server(main, debug=True, port=8080, cdn=False)
