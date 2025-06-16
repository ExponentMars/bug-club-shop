from flask import Flask, render_template, url_for, abort

app = Flask(__name__)

# 🐞 Static product data (you can update or add more products here)
products = [
    {
        "id": 1,
        "name": "Blue Death Feigning Beetle",
        "price": 12.00,
        "desc": "A hardy, beginner-friendly desert beetle from the Sonoran desert. Easy to care for and long-lived.",
        "images": ["BDFB_onepack.jpg", "BDFB_Fivepack.jpg"]
    },
    {
        "id": 2,
        "name": "Blue Death Feigning Beetle (5-Pack)",
        "price": 50.00,
        "desc": "A discounted set of five Blue Death Feigning Beetles for serious collectors or educators.",
        "images": ["BDFB_Fivepack.jpg"]
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

# 🐞 Run the app in development mode
if __name__ == '__main__':
    app.run(debug=True)
