__all__ = ['feedback']
from pywebio.output import put_html
from pywebio.platform import seo
from pywebio.session import run_js
from src.settings import SEO_DESCRIPTION, SEO_TITLE
from src.utils.contents.index import FOOTER, HEADER, LANDING_PAGE_HEADING


@seo(SEO_TITLE, SEO_DESCRIPTION)
def feedback() -> None:
    run_js(HEADER)
    run_js(FOOTER)

    put_html(LANDING_PAGE_HEADING)
    put_html(r"""
    <iframe src="https://tally.so/embed/wdxRDw?hideTitle=1&alignLeft=1" width="100%" height="1050" frameborder="0" marginheight="0" marginwidth="0" title="Feedback"></iframe>
    """)
