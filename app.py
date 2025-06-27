# SaPay Flask Application
# Simple payment processing app with QR scanner integration

import os 
import qrcode 
from flask import Flask, render_template, jsonify, request, session
from services import get_user_banks, parse_promptpay_qr, convert_currency, process_payment, get_transaction_history
import random

app = Flask(__name__)
app.secret_key = "sapay_demo_key_123"  # simple secret key for sessions

# Home page route - main dashboard
@app.route('/')
def home():
    return render_template('index.html')

# EU bank selection page route
@app.route('/bank-selection')
def bank_selection():
    return render_template('bank_selection.html')

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

# Backend API routes for payment processing
@app.route('/api/banks')
def api_get_banks():
    # Get available EU bank accounts
    banks = get_user_banks()
    return jsonify(banks)

@app.route('/api/qr-scan', methods=['POST'])
def api_scan_qr():
    # Parse QR code data
    data = request.get_json()
    qr_code = data.get('qr_data', '')
    
    # For demo, also accept manual input
    if not qr_code:
        # Generate demo QR codes
        demo_merchants = [
            "promptpay://0891234567/500.00",
            "promptpay://0812345678/250.00"
        ]
        qr_code = random.choice(demo_merchants)
    
    result = parse_promptpay_qr(qr_code)
    return jsonify(result)

@app.route('/api/convert', methods=['POST'])
def api_convert_currency():
    # Convert EUR to THB
    data = request.get_json()
    amount_eur = float(data.get('amount_eur', 0))
    
    conversion = convert_currency(amount_eur)
    return jsonify(conversion)

@app.route('/api/process-payment', methods=['POST'])
def api_process_payment():
    # Main payment processing endpoint
    data = request.get_json()
    account_id = data.get('account_id')
    merchant_phone = data.get('merchant_phone')
    amount_eur = float(data.get('amount_eur'))
    
    # Store payment details in session
    session['last_payment'] = {
        'account_id': account_id,
        'merchant_phone': merchant_phone,
        'amount_eur': amount_eur
    }
    
    result = process_payment(account_id, merchant_phone, amount_eur)
    return jsonify(result)

@app.route('/api/transactions')
def api_get_transactions():
    # Get transaction history
    transactions = get_transaction_history()
    return jsonify(transactions)

# Run the application with SSL for camera access
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, ssl_context='adhoc')
