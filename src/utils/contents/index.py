from src.settings import CONTACT_EMAIL, GUMROAD_URL

# This page contains all the html contents corresponding to `src/index.py`

# Header
# ^^^^^^
HEADER = """
$('#favicon32,#favicon16').remove();
$('head').append('<link rel="icon" type="image/x-icon" href="/static/favicon/burplist.png">')
"""

# Footer
# ^^^^^^
FOOTER = f"""
$('FOOTER').html('👉 <a href="{GUMROAD_URL}" target="_blank">Download CSV</a> | ✉️ <a href="mailto:{CONTACT_EMAIL}" target="_blank">Contact</a> | 💡 <a href="/feedback">Feedback</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
"""


LOAD_CSS = r"""
<style>
.img {
    width: auto;
    height: auto;
    max-width: 400;
    max-height: 300px;
    border:2px solid #fff;
    -moz-box-shadow: 10px 10px 5px #ccc;
    -webkit-box-shadow: 10px 10px 5px #ccc;
    box-shadow: 10px 10px 5px #ccc;
    -moz-border-radius:25px;
    -webkit-border-radius:25px;
    border-radius:25px;
}
</style>
"""

LANDING_PAGE_HEADING = r"""
<h1 align="center"><strong>Burplist</strong></h1>
"""

PRODUCT_HUNT_FEATURED_BANNER = r"""
<div align="center"><a href="https://www.producthunt.com/posts/burplist?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-burplist" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=304966&theme=light" alt="Burplist - Free price comparison tool for craft beers | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a></div>
"""

LANDING_PAGE_SUBHEADING = r"""
<h3 align="center">Search Engine for Craft Beers 🍻 in Singapore</h1>
<p align="center">
    <img alt="Cheers" class="img" width="50%" height="50%" src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
"""

LANDING_PAGE_DESCRIPTION = r"""
# What is Burplist?

🔎 A free **search engine** for craft beers in Singapore.
📊 **Compare** craft beer prices online with a simple search.
❤️ Search for the cheapest **craft beer** in Singapore.
💯 Prices are updated **daily**.

## What is craft beer?

🤤 To simply put, craft beers are the more **delicious** alternative to your mainstream beers.
🍻 In terms of styles, flavors, and aroma, craft beers are usually more **diverse** in these aspects.
✨ Craft beers are usually brewed in smaller quantities by passionate brewers who care more about **quality** than quantity.

## How to use?

🛒 Shopping for beers? Simply enter any beer _brand_, _style_, or _name_ in the search bar and hit _"Enter"_.
🤑 Prices are ordered starting from the **lowest to highest**.
🔙 To return to this main page, simply hit _"Ctrl/Cmd + R"_ to refresh the page.


## Is this free?

🥳 Short answer: Yes.
🙌 Long answer: _Yessssssssssss_.
"""

DOWNLOAD_DESCRIPTION = f"""
## Can I download the data in a spreadsheet?

🎁 Yes. Gain full access to **over 2,500+** unique craft beer prices and information from **10+ different websites**.
👉 Click **[here]({GUMROAD_URL})** to view and download.
"""
