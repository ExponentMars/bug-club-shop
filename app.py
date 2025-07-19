from flask import Flask, render_template, url_for, abort

app = Flask(__name__)

# 🐞 Static product data (you can update or add more products here)
# Each product should follow this structure:
'''
    {
        "id": ,
        "name": "",
        "price": ,
        "desc": "",
        "images": ["", ""],
        "category": "",
        "shopify_buy_button":""""""
    }
'''

products = [
    {
        "id": 1,
        "name": "Blue Death Feigning Beetle",
        "price": 12.00,
        "desc": "A hardy, beginner-friendly desert beetle from the Sonoran desert. Easy to care for and long-lived.",
        "images": ["BDFB_onepack.jpg", "BDFB_Fivepack.jpg"],
        "category": "Beetles",
        "shopify_buy_button":"""<div id='product-component-1750123288781'></div><script type="text/javascript">/*<![CDATA[*/(function () { var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js'; if (window.ShopifyBuy) { if (window.ShopifyBuy.UI) { ShopifyBuyInit(); } else { loadScript(); } } else { loadScript(); } function loadScript() { var script = document.createElement('script'); script.async = true; script.src = scriptURL; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script); script.onload = ShopifyBuyInit; } function ShopifyBuyInit() { var client = ShopifyBuy.buildClient({ domain: 'dpd4di-jb.myshopify.com', storefrontAccessToken: 'c13ce63af0fa528eefd684a1445824d9', }); ShopifyBuy.UI.onReady(client).then(function (ui) { ui.createComponent('product', { id: '9841388323118', node: document.getElementById('product-component-1750123288781'), moneyFormat: '%24%7B%7Bamount%7D%7D', options: { "product": { "styles": { "product": { "@media (min-width: 601px)": { "max-width": "calc(25% - 20px)", "margin-left": "20px", "margin-bottom": "50px" } }, "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px", "padding-left": "69px", "padding-right": "69px" } }, "contents": { "img": false, "title": false, "price": false }, "text": { "button": "Add to cart" } }, "productSet": { "styles": { "products": { "@media (min-width: 601px)": { "margin-left": "-20px" } } } }, "modalProduct": { "contents": { "img": false, "imgWithCarousel": true, "button": false, "buttonWithQuantity": true }, "styles": { "product": { "@media (min-width: 601px)": { "max-width": "100%", "margin-left": "0px", "margin-bottom": "0px" } }, "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px", "padding-left": "69px", "padding-right": "69px" } }, "text": { "button": "Add to cart" } }, "option": {}, "cart": { "styles": { "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px" } }, "text": { "total": "Subtotal", "button": "Checkout" }, "contents": { "note": true } }, "toggle": { "styles": { "toggle": { "background-color": "#ffd700", ":hover": { "background-color": "#e6c200" }, ":focus": { "background-color": "#e6c200" } }, "count": { "color": "#000000", ":hover": { "color": "#000000" } }, "iconPath": { "fill": "#000000" } } }}, }); }); }})();/*]]>*/</script>"""

    },
    {
        "id": 2,
        "name": "Blue Death Feigning Beetle (5-Pack)",
        "price": 50.00,
        "desc": "A discounted pack of five Blue Death Feigning Beetles.",
        "images": ["BDFB_Fivepack.jpg"],
        "category": "Beetles",
        "shopify_buy_button":"""<div id='product-component-1750123393573'></div><script type="text/javascript">/*<![CDATA[*/(function () { var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js'; if (window.ShopifyBuy) { if (window.ShopifyBuy.UI) { ShopifyBuyInit(); } else { loadScript(); } } else { loadScript(); } function loadScript() { var script = document.createElement('script'); script.async = true; script.src = scriptURL; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script); script.onload = ShopifyBuyInit; } function ShopifyBuyInit() { var client = ShopifyBuy.buildClient({ domain: 'dpd4di-jb.myshopify.com', storefrontAccessToken: 'c13ce63af0fa528eefd684a1445824d9', }); ShopifyBuy.UI.onReady(client).then(function (ui) { ui.createComponent('product', { id: '9843630342446', node: document.getElementById('product-component-1750123393573'), moneyFormat: '%24%7B%7Bamount%7D%7D', options: { "product": { "styles": { "product": { "@media (min-width: 601px)": { "max-width": "calc(25% - 20px)", "margin-left": "20px", "margin-bottom": "50px" } }, "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px", "padding-left": "69px", "padding-right": "69px" } }, "contents": { "img": false, "title": false, "price": false }, "text": { "button": "Add to cart" } }, "productSet": { "styles": { "products": { "@media (min-width: 601px)": { "margin-left": "-20px" } } } }, "modalProduct": { "contents": { "img": false, "imgWithCarousel": true, "button": false, "buttonWithQuantity": true }, "styles": { "product": { "@media (min-width: 601px)": { "max-width": "100%", "margin-left": "0px", "margin-bottom": "0px" } }, "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px", "padding-left": "69px", "padding-right": "69px" } }, "text": { "button": "Add to cart" } }, "option": {}, "cart": { "styles": { "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px" } }, "text": { "total": "Subtotal", "button": "Checkout" }, "contents": { "note": true } }, "toggle": { "styles": { "toggle": { "background-color": "#ffd700", ":hover": { "background-color": "#e6c200" }, ":focus": { "background-color": "#e6c200" } }, "count": { "color": "#000000", ":hover": { "color": "#000000" } }, "iconPath": { "fill": "#000000" } } }}, }); }); }})();/*]]>*/</script>"""

    },
    {
        "id": 3,
        "name": "Test Tube Portal -- 16mm OD Test Tubes",
        "price": 10.00,
        "desc": "The ideal setup for young ant colonies, this test tube portal allows for easy observation and care. Use it to move ants to new test tubes or as a foraging area. The test tube ports ",
        "images": ["P1130002.JPG", "P1130008.JPG","P1130011.JPG"],
        "category": "Formicariums",
        "shopify_buy_button":"""<div id='product-component-1752966556665'></div><script type="text/javascript">/*<![CDATA[*/(function () { var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js'; if (window.ShopifyBuy) { if (window.ShopifyBuy.UI) { ShopifyBuyInit(); } else { loadScript(); } } else { loadScript(); } function loadScript() { var script = document.createElement('script'); script.async = true; script.src = scriptURL; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script); script.onload = ShopifyBuyInit; } function ShopifyBuyInit() { var client = ShopifyBuy.buildClient({ domain: 'dpd4di-jb.myshopify.com', storefrontAccessToken: 'c13ce63af0fa528eefd684a1445824d9', }); ShopifyBuy.UI.onReady(client).then(function (ui) { ui.createComponent('product', { id: '9871812002094', node: document.getElementById('product-component-1752966556665'), moneyFormat: '%24%7B%7Bamount%7D%7D', options: { "product": { "styles": { "product": { "@media (min-width: 601px)": { "max-width": "calc(25% - 20px)", "margin-left": "20px", "margin-bottom": "50px" } }, "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px", "padding-left": "69px", "padding-right": "69px" } }, "contents": { "img": false, "title": false, "price": false }, "text": { "button": "Add to cart" } }, "productSet": { "styles": { "products": { "@media (min-width: 601px)": { "margin-left": "-20px" } } } }, "modalProduct": { "contents": { "img": false, "imgWithCarousel": true, "button": false, "buttonWithQuantity": true }, "styles": { "product": { "@media (min-width: 601px)": { "max-width": "100%", "margin-left": "0px", "margin-bottom": "0px" } }, "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px", "padding-left": "69px", "padding-right": "69px" } }, "text": { "button": "Add to cart" } }, "option": {}, "cart": { "styles": { "button": { "color": "#000000", ":hover": { "color": "#000000", "background-color": "#e6c200" }, "background-color": "#ffd700", ":focus": { "background-color": "#e6c200" }, "border-radius": "0px" } }, "text": { "total": "Subtotal", "button": "Checkout" }, "contents": { "note": true } }, "toggle": { "styles": { "toggle": { "background-color": "#ffd700", ":hover": { "background-color": "#e6c200" }, ":focus": { "background-color": "#e6c200" } }, "count": { "color": "#000000", ":hover": { "color": "#000000" } }, "iconPath": { "fill": "#000000" } } }}, }); }); }})();/*]]>*/</script>"""
    }

]

# 🏠 Homepage: Product Grid
@app.route('/')
def index():
    return render_template('index.html', products=products)

# 📄 Individual Product Page
@app.route('/product/<int:product_id>')
def product(product_id):
    product_data = next((p for p in products if p['id'] == product_id), None)
    if not product_data:
        abort(404)
    return render_template('product.html', product=product_data)

@app.route('/category/<category_name>')
def category(category_name):
    filtered_products = [p for p in products if p['category'].lower() == category_name.lower()]
    return render_template('category.html', products=filtered_products, category_name=category_name.title())

# 🐞 Run the app in development mode
if __name__ == '__main__':
    app.run()
