# Basic data models for SaPay backend
# Simple classes to store payment and bank information

import time
import random

class BankAccount:
    def __init__(self, account_id, bank_name, balance, currency="EUR"):
        self.account_id = account_id
        self.bank_name = bank_name
        self.balance = balance
        self.currency = currency
        self.account_holder = "Demo User"
        self.iban = "DE89370400440532013000"  # fake IBAN for demo

    def can_withdraw(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance = self.balance - amount
            return True
        return False

class ThaiMerchant:
    def __init__(self, merchant_id, business_name, phone_number):
        self.merchant_id = merchant_id
        self.business_name = business_name  
        self.phone_number = phone_number
        self.accepts_promptpay = True

class PaymentTransaction:
    def __init__(self):
        self.transaction_id = "txn_" + str(int(time.time())) + str(random.randint(100, 999))
        self.amount_eur = 0
        self.amount_thb = 0
        self.exchange_rate = 38.5  # roughly EUR to THB
        self.status = "pending"  # pending, completed, failed
        self.timestamp = int(time.time())
        self.eu_account_id = ""
        self.thai_merchant_id = ""
        self.sapay_fee = 0.39  # euros

    def calculate_thb_amount(self, eur_amount):
        self.amount_eur = eur_amount
        # add some random variation to exchange rate
        rate_variation = random.uniform(-0.2, 0.2)
        self.exchange_rate = 38.5 + rate_variation
        self.amount_thb = eur_amount * self.exchange_rate
        return self.amount_thb

# Global storage for demo purposes
# In real app this would be a database
BANK_ACCOUNTS = {}
THAI_MERCHANTS = {}
TRANSACTIONS = {}

def setup_demo_data():
    # Create some demo bank accounts
    deutsche_bank = BankAccount("DB_001", "Deutsche Bank", 2847.50)
    bnp_paribas = BankAccount("BNP_001", "BNP Paribas", 1205.75) 
    ing_bank = BankAccount("ING_001", "ING Bank", 3156.20)
    
    BANK_ACCOUNTS["DB_001"] = deutsche_bank
    BANK_ACCOUNTS["BNP_001"] = bnp_paribas
    BANK_ACCOUNTS["ING_001"] = ing_bank
    
    # Create demo Thai merchants
    seven_eleven = ThaiMerchant("TH_001", "7-Eleven Store", "0891234567")
    family_mart = ThaiMerchant("TH_002", "FamilyMart", "0812345678")
    
    THAI_MERCHANTS["0891234567"] = seven_eleven
    THAI_MERCHANTS["0812345678"] = family_mart

# Initialize demo data when module loads
setup_demo_data()
