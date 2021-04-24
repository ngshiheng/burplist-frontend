from pywebio import start_server
from pywebio.input import TEXT, input
from pywebio.output import put_markdown, put_text
from pywebio.session import set_env


def main():
    put_markdown(r"""
    # Burplist
    > Find out where to purchase the cheapest beer in Singapore 🇸🇬
    """, lstrip=True)

    set_env(title='Burplist')

    while True:

        search = input(
            'What are you looking for? 🍻', type=TEXT, placeholder='What are you thisting for...',
            help_text='Example: Road Hog', required=True,
        )

        put_text(search)


if __name__ == '__main__':
    start_server(main, debug=True, port=8080, cdn=False)
