from flask import Flask, render_template
from flask import request, redirect

products = {
  "sku01": { 
      "id": "sku01", 
      "name": "Pen", 
      "price": 15, 
      "desc": "This is a pen",
      "image": "data:image/jpeg;base64,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"
      },
  "sku02": { 
      "id": "sku02", 
      "name": "Cup", 
      "price": 80, 
      "desc": "This is a cup",
      "image": "https://www.ikea.com/my/en/images/products/vaerdera-coffee-cup-and-saucer__0711123_PE727991_S5.JPG"
      },
  "sku03": { 
      "id": "sku03", 
      "name": "Notebook", 
      "price": 25, 
      "desc": "This is a notebook",
      "image": "https://poppin.imgix.net/products/2018/Medium-Spiral-Notebook_Storm-Velvet_PDP_02.jpg"
     },
  "sku04": { 
      "id": "sku04", 
      "name": "Stapler", 
      "price": 30, 
      "desc": "This is a stapler",
      "image": "https://images-na.ssl-images-amazon.com/images/I/61hLan93NbL._AC_SX466_.jpg"
      },
}

cart = {
    "sku01": 2,
    "sku02": 5
}
app = Flask(__name__)

@app.route("/")
def myshop():
    total = 0
    for key in cart:
        qty = cart[key]
        item = products[key]
        total += item['price'] * qty

    return render_template("myShop.html", products=products, cart=cart, total=total)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)

@app.route('/product/<id>/edit', methods = ['GET', 'POST'])
def edit(id):
    prod = products[id]
    if request.method == 'POST':
        prod['name'] = request.form['name']
        prod['price'] = int(request.form['price'])
        prod['desc'] = request.form['desc']
        prod['image'] = request.form['image']
        return redirect('/product/' + id)
    return render_template('product-edit.html', product=prod)

@app.route("/cart/edit")
def cartEdit():
  return render_templates("cart-edit")


