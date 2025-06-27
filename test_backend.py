# Simple test script for SaPay backend
# Run this to test the payment processing without frontend

import sys
import os

# Add current directory to path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services import get_user_banks, parse_promptpay_qr, convert_currency, process_payment
from models import BANK_ACCOUNTS

def test_banks():
    print("=== Testing Bank Accounts ===")
    banks = get_user_banks()
    for bank in banks:
        print(f"Bank: {bank['bank_name']}, Balance: €{bank['balance']}")
    print()

def test_qr_parsing():
    print("=== Testing QR Code Parsing ===")
    test_qr = "promptpay://0891234567/500.00"
    result = parse_promptpay_qr(test_qr)
    if result['success']:
        print(f"Merchant: {result['business_name']}")
        print(f"Phone: {result['phone_number']}")
        print(f"Amount: ฿{result['suggested_amount_thb']}")
    else:
        print(f"Error: {result['error']}")
    print()

def test_currency_conversion():
    print("=== Testing Currency Conversion ===")
    amount_eur = 13.0
    conversion = convert_currency(amount_eur)
    print(f"€{amount_eur} = ฿{conversion['amount_thb']}")
    print(f"Exchange rate: {conversion['exchange_rate']}")
    print(f"SaPay fee: ฿{conversion['sapay_fee_thb']}")
    print(f"Savings vs ATM: ฿{conversion['savings_thb']}")
    print()

def test_full_payment():
    print("=== Testing Full Payment Process ===")
    
    # Use first available bank account
    account_id = "DB_001"
    merchant_phone = "0891234567" 
    amount_eur = 13.0
    
    print(f"Processing payment...")
    print(f"Account: {account_id}")
    print(f"Merchant: {merchant_phone}")
    print(f"Amount: €{amount_eur}")
    
    # Check initial balance
    initial_balance = BANK_ACCOUNTS[account_id].balance
    print(f"Initial balance: €{initial_balance}")
    
    # Process payment
    result = process_payment(account_id, merchant_phone, amount_eur)
    
    if result['success']:
        print("✅ Payment successful!")
        print(f"Transaction ID: {result['transaction_id']}")
        print(f"Amount charged: €{amount_eur + result['sapay_fee_eur']}")
        print(f"Thai amount: ฿{result['amount_thb']}")
        
        # Check final balance
        final_balance = BANK_ACCOUNTS[account_id].balance
        print(f"Final balance: €{final_balance}")
        print(f"Amount deducted: €{initial_balance - final_balance}")
    else:
        print("❌ Payment failed!")
        print(f"Error: {result['error']}")
    print()

def run_all_tests():
    print("SaPay Backend Test Suite")
    print("=" * 30)
    
    test_banks()
    test_qr_parsing()
    test_currency_conversion()
    test_full_payment()
    
    print("Tests completed!")

if __name__ == "__main__":
    run_all_tests() 