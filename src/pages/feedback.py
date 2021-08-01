__all__ = ['feedback']
from pywebio.output import put_html
from pywebio.platform import seo
from pywebio.session import run_js
from src.settings import SEO_DESCRIPTION, SEO_TITLE
from src.utils.contents.index import footer, header, landing_page_heading


@seo(SEO_TITLE, SEO_DESCRIPTION)
def feedback() -> None:
    run_js(header)
    run_js(footer)

    put_html(landing_page_heading)
    put_html(r"""
    <iframe src="https://tally.so/embed/wdxRDw?hideTitle=1&alignLeft=1" width="100%" height="1050" frameborder="0" marginheight="0" marginwidth="0" title="Feedback"></iframe>
    """)
