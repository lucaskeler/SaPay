import os 
import qrcode 
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/pin')
def pin():
    return render_template('pin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, ssl_context='adhoc')
