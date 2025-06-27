# SaPay - Cross-Border Mobile Payment Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

SaPay is an innovative cross-border payment platform that bridges EU open banking with Thailand's PromptPay system, eliminating costly ATM fees and poor exchange rates for European tourists in Thailand.

## 🎯 Business Innovation

**Problem**: European tourists lose €180 million annually to ATM fees and poor exchange rates in Thailand.

**Solution**: Direct connection between EU bank accounts and Thai PromptPay merchants, reducing transaction costs by 85%.

**Market Opportunity**: 77+ million tourist registrations annually in Thailand, with 40+ million from Europe.

## 💰 Value Proposition

- **Cost Savings**: €0.39 SaPay fee vs €5.70 traditional ATM withdrawal fee
- **Better Exchange Rates**: Real-time interbank rates vs tourist exchange rates
- **Convenience**: Pay directly at Thai merchants without cash conversion
- **Security**: EU banking standards with Thai payment integration

## 🚀 Key Features

### Cross-Border Payment Flow
- **EU Bank Integration**: Mock PSD2 open banking connection with 3 major banks
- **Real-Time Currency Conversion**: EUR ↔ THB with live exchange rates
- **PromptPay QR Integration**: Seamless Thai merchant payments
- **Transaction Processing**: End-to-end payment execution with status tracking

### User Experience
- **Mobile-First Design**: Optimized for tourist usage on smartphones
- **Multi-Step Security**: PIN verification and transaction confirmation
- **Live Feedback**: Real-time conversion display and savings calculation
- **Intuitive Navigation**: Clear payment flow with loading transitions

### Backend Capabilities (NEW)
- **Mock Banking APIs**: Simulated EU bank account management
- **Payment Processing**: Full transaction lifecycle from debit to credit
- **Currency Exchange**: Live rate simulation with realistic market variation
- **Transaction History**: In-memory storage and retrieval of payment records

## 🛠️ Technical Architecture

### Backend
- **Flask** (Python): Lightweight web framework for rapid prototyping
- **Mock Services**: Simulated EU banking and Thai PromptPay integration
- **RESTful APIs**: 5 endpoints for payment processing and bank management
- **In-Memory Storage**: Simple data persistence using Python dictionaries
- **Session Management**: Secure data persistence across payment flow

### Frontend
- **HTML5**: Modern semantic structure with accessibility
- **CSS3**: Responsive design with mobile-first approach
- **Vanilla JavaScript**: Lightweight, no external dependencies
- **AJAX Integration**: Frontend-backend communication via Fetch API
- **SessionStorage**: Client-side data persistence

### Libraries & APIs
- **Html5-QRCode**: Camera-based QR code scanning
- **Cleave.js**: Real-time currency input formatting
- **Backend APIs**: Custom payment processing endpoints

## 📁 Project Structure

```
SaPay/
├── README.md                # Project documentation
├── app.py                   # Flask application with routes & API endpoints
├── models.py                # Data models for banks, merchants, transactions
├── services.py              # Payment processing business logic
├── utils.py                 # Helper functions and utilities
├── test_backend.py          # Backend testing script
├── requirements.txt         # Python dependencies
│
├── templates/               # HTML templates with Jinja2
│   ├── base.html           # Base template with common layout
│   ├── index.html          # Home dashboard
│   ├── bank_selection.html # EU bank connection
│   ├── scanner.html        # QR code scanner interface
│   ├── payment.html        # Amount entry with savings display
│   ├── pin.html            # Security PIN entry
│   ├── loading.html        # Transition loading pages
│   └── success.html        # Payment confirmation
│
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Responsive stylesheet
│   ├── js/
│   │   ├── script.js       # QR scanner functionality
│   │   └── pages/          # Page-specific JavaScript
│   │       ├── currency_convert.js  # Currency conversion & savings
│   │       ├── bank_selection.js    # EU bank account selection
│   │       ├── pin.js              # PIN entry logic
│   │       └── timer.js            # Loading page transitions
│   └── img/                # Image assets
│
└── venv/                   # Virtual environment
```

## 💡 Implementation Highlights

### 1. Cross-Border Currency Conversion
```javascript
// Real-time EUR to THB conversion with savings calculation
const EXCHANGE_RATE = 38.45; // Mock live rate
const TRADITIONAL_FEE = 220; // THB ATM fee
const SAPAY_FEE = 15; // THB SaPay fee

function calculateSavings(thbAmount) {
    const savings = TRADITIONAL_FEE - SAPAY_FEE; // ฿205 saved per transaction
    return { savingsTHB: savings, savingsEUR: savings / EXCHANGE_RATE };
}
```

### 2. EU Bank Account Integration
```javascript
// Mock PSD2 open banking connection
const euBanks = [
    { name: 'Deutsche Bank', balance: 2847.50, currency: 'EUR' },
    { name: 'BNP Paribas', balance: 1205.75, currency: 'EUR' },
    { name: 'ING Bank', balance: 3156.20, currency: 'EUR' }
];
```

### 3. Secure Payment Flow
```javascript
// Multi-step verification with session persistence
sessionStorage.setItem('selectedBank', JSON.stringify(bank));
sessionStorage.setItem('paymentAmount', amount);
// PIN verification → Loading → Success confirmation
```

## 🔧 Backend Implementation

### API Endpoints
```
GET  /api/banks           - List available EU bank accounts
POST /api/qr-scan         - Parse PromptPay QR codes  
POST /api/convert         - EUR to THB currency conversion
POST /api/process-payment - Execute cross-border payment
GET  /api/transactions    - Retrieve transaction history
```

### Data Models (models.py)
```python
class BankAccount:
    - account_id, bank_name, balance, currency
    - can_withdraw(), withdraw() methods

class ThaiMerchant:
    - merchant_id, business_name, phone_number
    - PromptPay integration ready

class PaymentTransaction:
    - transaction_id, amounts, exchange_rate, status
    - calculate_thb_amount() with live rates
```

### Core Services (services.py)
- **get_user_banks()**: Retrieve EU bank accounts
- **parse_promptpay_qr()**: Parse Thai merchant QR codes
- **convert_currency()**: EUR/THB conversion with fees
- **process_payment()**: End-to-end payment execution
- **get_transaction_history()**: Payment record retrieval

### Demo Data
- **3 EU Banks**: Deutsche Bank (€2,847), BNP Paribas (€1,205), ING Bank (€3,156)
- **2 Thai Merchants**: 7-Eleven, FamilyMart with PromptPay IDs
- **Live Exchange Rate**: ~38.5 EUR/THB with realistic variation
- **Fee Structure**: €0.39 SaPay fee vs €5.70 traditional ATM fee

### Testing
Run backend tests independently:
```bash
python test_backend.py
```
Tests bank account access, QR parsing, currency conversion, and full payment flow.

## 🎬 Demo Flow (10 minutes)

1. **Problem Statement** (1 min): Tourist pain points and market opportunity
2. **Technical Architecture** (2 min): Frontend + Backend integration
3. **Live Demo** (5 min):
   - From home dashboard, click "Swap Card" (🔁) to select EU bank
   - Backend loads Deutsche Bank account (€2,847 balance) via `/api/banks`
   - Scan Thai merchant QR code (7-Eleven) - parsed via `/api/qr-scan`
   - Enter payment amount (฿500 = €13.00)
   - Backend calculates conversion via `/api/convert` - Save ฿205 vs traditional ATM
   - Complete secure PIN verification
   - Backend processes payment via `/api/process-payment`
   - View transaction confirmation with live data
4. **Backend Testing** (1 min): Show `python test_backend.py` results
5. **Business Model** (1 min): Revenue streams and scaling strategy

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser with camera access
- HTTPS support (for camera permissions)

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/sapay.git
cd sapay

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Access Application
- Open browser to `https://localhost:5001`
- Accept SSL certificate warning (self-signed for HTTPS camera access)
- Click "Swap Card" (🔁) to select your EU bank account

### Test Backend Only
```bash
# Test payment processing without frontend
python test_backend.py

# Test API endpoints directly
curl https://localhost:5001/api/banks
```

## 🔒 Security Considerations

### Current Implementation
- **PIN Verification**: 4-digit security PIN
- **Session Management**: Secure client-side storage
- **HTTPS**: SSL encryption for all communications

### Production Requirements
- **PSD2 Compliance**: Strong customer authentication
- **Thai Banking Regulations**: PromptPay partnership requirements
- **Data Protection**: GDPR compliance for EU customer data
- **Fraud Detection**: Real-time transaction monitoring

## 📈 Scaling Considerations

### Technical Scaling
- **Microservices Architecture**: Separate services for EU banking, Thai payments
- **API Gateway**: Centralized request handling and rate limiting
- **Database**: PostgreSQL for transaction history and user data
- **Real-Time Rates**: Integration with currency exchange APIs

### Business Scaling
- **Bank Partnerships**: PSD2-compliant EU bank integrations
- **PromptPay Integration**: Official Thai banking system connection
- **Regulatory Compliance**: Financial services licenses (EU & Thailand)
- **Multi-Currency Support**: Expand beyond EUR-THB corridor

## ✅ Current Implementation Status

### Frontend (Complete)
- ✅ Mobile-responsive UI with 7 pages
- ✅ QR code scanner with camera integration
- ✅ Currency formatting and amount persistence
- ✅ PIN entry system
- ✅ Multi-step payment flow

### Backend (NEW - Complete)
- ✅ 5 REST API endpoints
- ✅ Mock EU bank integration (3 banks)
- ✅ PromptPay QR code parsing
- ✅ Currency conversion with live rates
- ✅ Full payment processing pipeline
- ✅ Transaction history and status tracking
- ✅ Comprehensive test suite

### Technical Debt (For Production)
- 🔄 Replace in-memory storage with database
- 🔄 Add proper error handling and logging
- 🔄 Implement real banking API integration
- 🔄 Add authentication and authorization
- 🔄 Enhance security and compliance features

## 🎯 Next Steps

1. **MVP Validation**: Tourist user testing in Thailand
2. **Database Integration**: Replace in-memory storage with PostgreSQL
3. **Real Banking APIs**: Connect to actual PSD2 and PromptPay systems
4. **Security Enhancement**: Add encryption, authentication, fraud detection
5. **Regulatory Approval**: PSD2 and Thai banking compliance
6. **Pilot Program**: Limited rollout with select EU banks

## 📝 License

This project is licensed under the MIT License.

## 👥 Team

Built for cross-border fintech innovation, bridging European open banking with Southeast Asian payment systems.

---

*Eliminating financial friction for 40+ million European tourists annually.* 