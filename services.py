# Backend services for payment processing
# Simple functions to handle EU banking and Thai payments

import time
import random
from models import BANK_ACCOUNTS, THAI_MERCHANTS, TRANSACTIONS, PaymentTransaction

def get_user_banks():
    # Return list of available EU banks for selection
    banks = []
    for account_id, account in BANK_ACCOUNTS.items():
        bank_info = {
            "account_id": account_id,
            "bank_name": account.bank_name,
            "balance": account.balance,
            "currency": account.currency,
            "account_holder": account.account_holder
        }
        banks.append(bank_info)
    return banks

def check_bank_balance(account_id):
    # Simple balance check
    if account_id in BANK_ACCOUNTS:
        account = BANK_ACCOUNTS[account_id]
        return {
            "success": True,
            "balance": account.balance,
            "currency": account.currency
        }
    else:
        return {"success": False, "error": "Account not found"}

def parse_promptpay_qr(qr_string):
    # Basic QR code parsing for PromptPay
    # Expected format: "promptpay://phone_number/amount"
    try:
        if not qr_string.startswith("promptpay://"):
            return {"success": False, "error": "Invalid QR format"}
        
        # Remove the prefix and split by /
        qr_data = qr_string.replace("promptpay://", "")
        parts = qr_data.split("/")
        
        phone_number = parts[0]
        suggested_amount = 0
        if len(parts) > 1:
            suggested_amount = float(parts[1])
        
        # Look up merchant by phone number
        if phone_number in THAI_MERCHANTS:
            merchant = THAI_MERCHANTS[phone_number]
            return {
                "success": True,
                "merchant_id": merchant.merchant_id,
                "business_name": merchant.business_name,
                "phone_number": phone_number,
                "suggested_amount_thb": suggested_amount
            }
        else:
            return {"success": False, "error": "Merchant not found"}
    
    except Exception:
        return {"success": False, "error": "QR parsing failed"}

def calculate_exchange_rate():
    # Simple FX rate calculation with some randomness
    base_rate = 38.5
    # Add daily variation
    variation = random.uniform(-0.5, 0.5)
    current_rate = base_rate + variation
    
    return {
        "eur_to_thb": round(current_rate, 2),
        "timestamp": int(time.time()),
        "source": "mock_fx_api"
    }

def convert_currency(amount_eur):
    # Convert EUR to THB with current rate
    rate_info = calculate_exchange_rate()
    rate = rate_info["eur_to_thb"]
    
    amount_thb = amount_eur * rate
    sapay_fee_thb = 15  # 15 baht fee
    traditional_fee_thb = 220  # typical ATM fee
    savings_thb = traditional_fee_thb - sapay_fee_thb
    
    return {
        "amount_eur": amount_eur,
        "amount_thb": round(amount_thb, 2),
        "exchange_rate": rate,
        "sapay_fee_thb": sapay_fee_thb,
        "traditional_fee_thb": traditional_fee_thb,
        "savings_thb": savings_thb,
        "total_cost_thb": round(amount_thb + sapay_fee_thb, 2)
    }

def process_payment(account_id, merchant_phone, amount_eur):
    # Main payment processing function
    
    # Check if account exists and has sufficient balance
    if account_id not in BANK_ACCOUNTS:
        return {"success": False, "error": "Account not found"}
    
    account = BANK_ACCOUNTS[account_id]
    if not account.can_withdraw(amount_eur + 0.39):  # amount + SaPay fee
        return {"success": False, "error": "Insufficient balance"}
    
    # Check if merchant exists
    if merchant_phone not in THAI_MERCHANTS:
        return {"success": False, "error": "Merchant not found"}
    
    merchant = THAI_MERCHANTS[merchant_phone]
    
    # Create transaction record
    transaction = PaymentTransaction()
    transaction.eu_account_id = account_id
    transaction.thai_merchant_id = merchant.merchant_id
    
    # Calculate amounts
    thb_amount = transaction.calculate_thb_amount(amount_eur)
    
    # Simulate some processing time
    time.sleep(1)
    
    # Random chance of failure for realistic testing
    if random.random() < 0.05:  # 5% failure rate
        transaction.status = "failed"
        TRANSACTIONS[transaction.transaction_id] = transaction
        return {
            "success": False, 
            "error": "Payment network error",
            "transaction_id": transaction.transaction_id
        }
    
    # Process the payment
    total_charge_eur = amount_eur + transaction.sapay_fee
    if account.withdraw(total_charge_eur):
        transaction.status = "completed"
        
        # Store transaction
        TRANSACTIONS[transaction.transaction_id] = transaction
        
        return {
            "success": True,
            "transaction_id": transaction.transaction_id,
            "amount_eur": amount_eur,
            "amount_thb": round(thb_amount, 2),
            "exchange_rate": transaction.exchange_rate,
            "sapay_fee_eur": transaction.sapay_fee,
            "merchant_name": merchant.business_name,
            "timestamp": transaction.timestamp
        }
    else:
        transaction.status = "failed"
        TRANSACTIONS[transaction.transaction_id] = transaction
        return {"success": False, "error": "Payment processing failed"}

def get_transaction_history():
    # Get recent transactions for display
    transaction_list = []
    for txn_id, txn in TRANSACTIONS.items():
        merchant_name = "Unknown Merchant"
        if txn.thai_merchant_id:
            # Find merchant name
            for phone, merchant in THAI_MERCHANTS.items():
                if merchant.merchant_id == txn.thai_merchant_id:
                    merchant_name = merchant.business_name
                    break
        
        transaction_list.append({
            "transaction_id": txn_id,
            "amount_eur": txn.amount_eur,
            "amount_thb": round(txn.amount_thb, 2),
            "merchant_name": merchant_name,
            "status": txn.status,
            "timestamp": txn.timestamp
        })
    
    # Sort by timestamp, newest first
    transaction_list.sort(key=lambda x: x["timestamp"], reverse=True)
    return transaction_list[:10]  # Return last 10 transactions

def check_transaction_status(transaction_id):
    # Look up specific transaction
    if transaction_id in TRANSACTIONS:
        txn = TRANSACTIONS[transaction_id]
        return {
            "success": True,
            "transaction_id": transaction_id,
            "status": txn.status,
            "amount_eur": txn.amount_eur,
            "amount_thb": round(txn.amount_thb, 2),
            "timestamp": txn.timestamp
        }
    else:
        return {"success": False, "error": "Transaction not found"}
