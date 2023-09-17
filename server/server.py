from flask import Flask
from config import developer
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
@app.get("/api/about")
def about_me():
    return json.dumps(developer)

# example Products list for class 3 assignment
products = [{"name":"Raspberry pi 3"}, {"name":"Raspberry pi 4"}, {"name":"Raspberry pi Pico"}, {"name":"ESP32"}]
@app.get("/api/products")
def get_products():
    # products = []
    return json.dumps(products)

@app.get("/api/catalog")
def get_catalog():
    # products = []
    return json.dumps(len(products))


app.run(debug=True)

