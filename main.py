import os
import json
from scrapper import getData
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/covid19',methods=['GET','POST'])
def main():
    response=getData()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5001)
