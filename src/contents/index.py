from src.settings import CONTACT_EMAIL, GUMROAD_URL

# This page contains all the html contents corresponding to `src/index.py`

# Header
# ^^^^^^
header = """
$('#favicon32,#favicon16').remove();
$('head').append('<link rel="icon" type="image/x-icon" href="/static/favicon/burplist.png">')
"""

# Footer
# ^^^^^^
footer = f"""
$('footer').html('👉 <a href="">Download CSV</a> | ✉️ <a href="mailto:{CONTACT_EMAIL}">Contact</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
"""


load_css = r"""
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

landing_page_heading = r"""
<h1 align="center"><strong>Burplist</strong></h1>
"""

landing_page_subheading = r"""
<h3 align="center">🔍 A search engine for craft beers 🍻</h1>
<p align="center">
    <img alt="Cheers" class="img" width="50%" height="50%" src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
"""

landing_page_description = r"""
# What is Burplist?

🇸🇬 A collection of **craft beer** prices in Singapore at your fingertips.
🔎 Think of it as a **search engine** for craft beers in Singapore.

## What is craft beer?

🤤 To simply put, craft beers are the more **delicious** alternative to your mainstream beers.
🍻 In terms of styles, flavours and aroma, craft beers are usually more **diverse** in these aspects.
✨ Craft beers are usually brewed in smaller quantities by passionate brewers who care more about **quality** than quantity.

## How to use?

🛒 Shopping for beers? Simply enter any beer _brand_, _style_, or _name_ in the search bar and hit _"Submit"_.
🤑 Prices are ordered starting **from the lowest** to highest.
🔙 To return to this main page, simply hit _"Ctrl/Cmd + R"_ to refresh the page.

## Is this free?

🥳 Short answer: Yes.
🙌 Long answer: _Yessssssssssss_.
"""

download_description = f"""
## Can I download the data in a spreadsheet?

🎁 Yes. Gain full access to **over 2,000+** unique craft beer prices and information from **10+ different websites**.
👉 Click **[here]({GUMROAD_URL})** to view and download.
"""
