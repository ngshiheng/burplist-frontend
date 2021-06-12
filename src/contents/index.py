from src.settings import CONTACT_EMAIL

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


landing_page_heading = r"""
<h1 align="center"><strong>Burplist</strong></h1>
"""


landing_page_gif = r"""
<h3 align="center">🔍 A search engine for craft beers 🍻</h1>
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
    <img alt="Cheers" class="img" width="50%" height="50%" src="/static/gifs/landing_page.gif">
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

## Can I download the data in a spreadsheet?

🎁 Yes. Gain full access to **over 2,000** unique craft beer prices and information for **SGD$1 (limited time ⚡️)**.
👉 Click **[here](https://gumroad.com/l/burplist/welcomeaboard10)** to view and download.
"""


no_results = r"""
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
    <img alt="No results found" class="img" width="50%" height="50%" src="/static/gifs/no_results.gif">
</p>
"""
