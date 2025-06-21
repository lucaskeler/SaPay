# SaPay Flask Application
# Simple payment processing app with QR scanner integration

import os 
import qrcode 
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Home page route - main dashboard
@app.route('/')
def home():
    return render_template('index.html')

# QR scanner page route
@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

# Loading transition page route
@app.route('/loading')
def loading():
    return render_template('loading.html')

# Payment amount entry page route
@app.route('/payment')
def payment():
    return render_template('payment.html')

# PIN entry page route
@app.route('/pin')
def pin():
    return render_template('pin.html')

# Payment success confirmation page route
@app.route('/success')
def success():
    return render_template('success.html')

# Run the application with SSL for camera access
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, ssl_context='adhoc')
