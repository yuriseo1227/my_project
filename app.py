from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb://sparta-yuri:sparta123!@13.125.210.185',27017)
db = client.dbsparta

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')