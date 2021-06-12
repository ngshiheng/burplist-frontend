mail_to = 'hello@burplist.me'

google_adsense = """$('head').append('<script data-ad-client="ca-pub-8667164348741019" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>')"""

header = f"""
$('#favicon32,#favicon16').remove();
$('head').append('<link rel="icon" type="image/x-icon" href="/static/favicon/burplist.png">')
"""

footer = f"""
$('footer').html('👉 <a href="https://gumroad.com/l/burplist/welcomeaboard10">Download CSV</a> | ✉️ <a href="mailto:{mail_to}">Contact</a> | 📃 <a href="/terms">Terms of Use</a> | 🔏 <a href="/privacy">Privacy Policy</a>')
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
    <img class="img" width="50%" height="50%" src="/static/gifs/home_page.gif">
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
    <img class="img" width="50%" height="50%" src="/static/gifs/no_results.gif">
</p>
"""


amplitude_tracking = r"""
$('head').append('<script type="text/javascript">(function(e,t){var n=e.amplitude||{_q:[],_iq:{}};var r=t.createElement("script") ;r.type="text/javascript" ;r.integrity="sha384-u0hlTAJ1tNefeBKwiBNwB4CkHZ1ck4ajx/pKmwWtc+IufKJiCQZ+WjJIi+7C6Ntm" ;r.crossOrigin="anonymous";r.async=true ;r.src="https://cdn.amplitude.com/libs/amplitude-8.1.0-min.gz.js" ;r.onload=function(){if(!e.amplitude.runQueuedFunctions){console.log("[Amplitude] Error: could not load SDK")}};var i=t.getElementsByTagName("script")[0];i.parentNode.insertBefore(r,i) ;function s(e,t){e.prototype[t]=function(){this._q.push([t].concat(Array.prototype.slice.call(arguments,0)));return this}}var o=function(){this._q=[];return this};var a=["add","append","clearAll","prepend","set","setOnce","unset","preInsert","postInsert","remove"] ;for(var c=0;c<a.length;c++){s(o,a[c])}n.Identify=o;var u=function(){this._q=[] ;return this};var l=["setProductId","setQuantity","setPrice","setRevenueType","setEventProperties"] ;for(var p=0;p<l.length;p++){s(u,l[p])}n.Revenue=u ;var d=["init","logEvent","logRevenue","setUserId","setUserProperties","setOptOut","setVersionName","setDomain","setDeviceId","enableTracking","setGlobalUserProperties","identify","clearUserProperties","setGroup","logRevenueV2","regenerateDeviceId","groupIdentify","onInit","logEventWithTimestamp","logEventWithGroups","setSessionId","resetSessionId"] ;function v(e){function t(t){e[t]=function(){e._q.push([t].concat(Array.prototype.slice.call(arguments,0)))}}for(var n=0;n<d.length;n++){t(d[n])}}v(n);n.getInstance=function(e){e=(!e||e.length===0?"$default_instance":e).toLowerCase() ;if(!Object.prototype.hasOwnProperty.call(n._iq,e)){n._iq[e]={_q:[]};v(n._iq[e])}return n._iq[e]};e.amplitude=n})(window,document); amplitude.getInstance().init("b5c55c2974a58b1c85cdd80332431d44");</script>')
"""

google_analytics = r"""
$('head').append('<script async src="https://www.googletagmanager.com/gtag/js?id=G-YW0GRZJ8MT"></script>')
$('head').append('<script>window.dataLayer=window.dataLayer || []; function gtag(){dataLayer.push(arguments);}gtag('js', new Date()); gtag('config', 'G-YW0GRZJ8MT');</script>')
"""
