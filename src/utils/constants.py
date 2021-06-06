favicon_url = "https://img.icons8.com/plasticine/100/000000/beer-glass.png"

mail_to = 'hello@burplist.me'

header = f"""
$('#favicon32,#favicon16').remove();
$('head').append('<link rel="icon" type="image/x-icon" href="{favicon_url}">')
"""

footer = f"""
$('footer').html('📬 <a href="mailto:{mail_to}">Contact Us</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
"""

landing_page_heading = r"""
<h1 align="center"><strong>Burplist</strong></h1>
"""


landing_page_gif = r"""
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
"""

landing_page_description = r"""
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
"""


product_not_found_gif = r"""
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
</p>
"""
