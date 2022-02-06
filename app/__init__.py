# !/user/bin/env python3
#-*-coding utf8 -*-
"""Sample hello worrld Flask app"""



from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, world</h1>"

@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list =  "".join(
        "<li>%s</li>" % product for product in product_list
        )
    return "<ul>%s</ul>" % bullet_list 

@app.route("/about", methods=["GET"])
def aboutme():
    me = {
        "first_name":"Will",
        "last_name": "Cisneros",
        "hobbies": "DIY stuff",
        "active": True 
    }
    return me
