# Utility functions for SaPay
# Helper functions used across the application

import time
import random
import string

def generate_transaction_id():
    # Simple transaction ID generator
    timestamp = str(int(time.time()))
    random_part = ''.join(random.choices(string.digits, k=4))
    return f"TXN_{timestamp}_{random_part}"

def format_currency(amount, currency="EUR"):
    # Basic currency formatting
    if currency == "EUR":
        return f"€{amount:.2f}"
    elif currency == "THB":
        return f"฿{amount:.2f}"
    else:
        return f"{amount:.2f} {currency}"

def validate_phone_number(phone):
    # Simple Thai phone number validation
    # Thai mobile numbers start with 08 or 09 and are 10 digits
    phone = phone.replace("-", "").replace(" ", "")
    if len(phone) == 10 and phone.startswith(('08', '09')):
        return True
    return False

def calculate_savings(sapay_fee_thb=15, atm_fee_thb=220):
    # Calculate savings compared to traditional ATM
    savings = atm_fee_thb - sapay_fee_thb
    return {
        "sapay_fee": sapay_fee_thb,
        "atm_fee": atm_fee_thb,
        "savings": savings,
        "savings_percentage": round((savings / atm_fee_thb) * 100, 1)
    }

def mock_api_delay(min_delay=0.5, max_delay=2.0):
    # Simulate realistic API response times
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    return delay

def log_transaction(transaction_data):
    # Simple logging function (in real app would use proper logging)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Transaction: {transaction_data}")

def generate_qr_demo_data():
    # Generate some demo QR codes for testing
    demo_qrs = [
        "promptpay://0891234567/500.00",  # 7-Eleven
        "promptpay://0812345678/250.00",  # FamilyMart
        "promptpay://0898765432/750.00",  # Restaurant
    ]
    return random.choice(demo_qrs)
