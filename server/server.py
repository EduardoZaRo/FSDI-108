from flask import Flask, request
from config import developer,db
import json

app = Flask("server")

@app.get("/")
def hello():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "Im the test bruh"

@app.get("/name")
def name():
    return "Irvin Eduardo Zavala Roman"


###########################################
###########################################
######         Products API        ########
###########################################
###########################################
def fix_id(record):
    record["_id"] = str(record["_id"])
    return record

@app.get("/api/about")
def about_me():
    return json.dumps(developer)

@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for product in cursor:
        products.append(fix_id(product))
    return json.dumps(products)

@app.post("/api/products")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    print(product)
    # return json.dumps(product, default=str)
    return json.dumps(fix_id(product))

@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for product in cursor:
        cat = product["category"]
        if cat not in categories:
            categories.append(cat)
    categories.sort()
    return json.dumps(categories)

@app.get("/api/products/<category>")
def get_by_category(category):
    cursor = db.products.find({"category":category})
    products = []
    for product in cursor:
        products.append(fix_id(product))
    return json.dumps(products)

app.run(debug=True)

