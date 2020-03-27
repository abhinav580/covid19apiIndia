import os
import json
from scrapper import getData
from flask import Flask, request, jsonify, render_template
from json2html import *
app = Flask(__name__)

@app.route('/api/v1.0/covid19',methods=['GET','POST'])
def write():
    response=getData()
    f = open("templates/index.html","w")
    htm=json2html.convert(json=response)
    f.write(htm)
    f.close()
    return render_template("index.html")
if __name__ == '__main__':
    app.run()
