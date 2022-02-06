# !/user/bin/env python3
#-*-coding utf8 -*-
"""Sample hello worrld Flask app"""



from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, world</h1>"