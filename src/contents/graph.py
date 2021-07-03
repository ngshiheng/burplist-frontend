from typing import Any

from pyg2plot import Plot
from pywebio.output import PopupSize, close_popup, popup, put_html
from src.utils.search import get_product_price_history


def plot_line_graph(data: list[dict[str, Any]]) -> None:
    line = Plot('Line')
    line.set_options({
        'data': data,
        'xField': 'date',
        'yField': 'price',
        'smooth': True,
        'lineStyle': {'lineWidth': 3, },
        'point': {
            'size': 5,
            'shape': 'diamond',
            'style': {
                'fill': 'white',
                'stroke': '#5B8FF9',
                'lineWidth': 2,
            },
        }
    })
    put_html(line.render_notebook())


def show_price_history_graph(self, product: dict[str, Any]) -> None:
    """
    Shows a popup rendering a line graph of the beer's historical price
    """
    @popup(title=product['name'], size=PopupSize.NORMAL)
    def show() -> None:
        product_prices = get_product_price_history(product['id'])
        if not product_prices:
            close_popup()
            return None

        data = [
            {
                'date': price.updated_on.strftime('%d %b %y'),
                'price': float(f'{price.price: .2f}'),
            } for price in product_prices
        ]
        plot_line_graph(data)
    show()
