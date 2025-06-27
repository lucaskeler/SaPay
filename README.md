# SaPay - Cross-Border Mobile Payment Platform
**FinTech Innovation MVP: EU-Thailand Payment Corridor**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

SaPay is an innovative cross-border payment platform that bridges EU open banking with Thailand's PromptPay system, eliminating costly ATM fees and poor exchange rates for European tourists in Thailand.

**Assignment**: FinTech Business Model MVP Implementation  
**Focus**: Demonstrating technical feasibility of cross-border payment innovation  
**Market**: €180M annual tourist payment friction in EU-Thailand corridor

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

### Backend Capabilities 
- **Mock Banking APIs**: Simulated EU bank account management
- **Payment Processing**: Full transaction lifecycle from debit to credit
- **Currency Exchange**: Live rate simulation with realistic market variation
- **Transaction History**: In-memory storage and retrieval of payment records

## 🛠️ Technical Architecture & Technology Stack

### Programming Language & Framework Choices

**Python + Flask Architecture**
- **Language**: Python 3.8+ for rapid FinTech prototyping and financial calculations
- **Framework**: Flask - lightweight, minimal boilerplate for MVP development
- **Paradigm**: RESTful API design with separation of concerns (MVC pattern)
- **Rationale**: Python's extensive financial libraries, Flask's simplicity for quick iteration, and strong community support for payment integrations

### Backend Architecture
- **Flask** (Python): Lightweight web framework optimized for rapid prototyping
- **Mock Services**: Simulated EU banking (PSD2) and Thai PromptPay integration
- **RESTful APIs**: 5 endpoints for payment processing and bank management
- **In-Memory Storage**: Python dictionaries for MVP (PostgreSQL for production)
- **Session Management**: Secure data persistence across payment flow
- **Modular Design**: Separate models, services, and utilities for maintainability

### Frontend Architecture
- **HTML5**: Semantic structure optimized for mobile-first financial UI
- **CSS3**: Responsive design with custom properties for consistent theming
- **Vanilla JavaScript**: Zero external dependencies for faster loading and security
- **AJAX Integration**: Fetch API for seamless backend communication
- **Progressive Enhancement**: Core functionality works without JavaScript
- **SessionStorage**: Client-side persistence for payment flow continuity

### Libraries & Dependencies
- **Html5-QRCode**: Camera-based QR code scanning for PromptPay integration
- **Cleave.js**: Real-time currency input formatting for better UX
- **pyOpenSSL**: HTTPS support for camera access and secure communication
- **Custom APIs**: Backend payment processing endpoints

### Python Dependencies (requirements.txt)

**Core Web Framework:**
- `Flask==3.1.1` - Lightweight web framework for rapid development
- `Werkzeug==3.1.3` - WSGI web application library
- `Jinja2==3.1.6` - Template engine for HTML rendering
- `itsdangerous==2.2.0` - Secure data serialization
- `MarkupSafe==3.0.2` - Safe string handling for templates

**Security & HTTPS:**
- `pyOpenSSL==25.1.0` - SSL/TLS support for HTTPS camera access
- `cryptography==45.0.3` - Cryptographic functions and SSL support
- `cffi==1.17.1` - Foreign function interface for cryptography
- `pycparser==2.22` - C parser for cryptographic operations

**Payment & API Integration:**
- `qrcode==8.2` - QR code generation for PromptPay integration
- `requests==2.32.3` - HTTP library for external API calls
- `urllib3==2.4.0` - HTTP client library
- `certifi==2025.4.26` - Certificate authority bundle for SSL verification

**Application Support:**
- `python-dotenv==1.1.0` - Environment variable management
- `click==8.2.1` - Command line interface creation
- `blinker==1.9.0` - Signal/event system for Flask
- `typing_extensions==4.14.0` - Extended type hints
- `charset-normalizer==3.4.2` - Character encoding detection
- `idna==3.10` - Internationalized domain names support

### Architecture Mapping to Conceptual Innovation

**Innovation**: Direct EU bank account to Thai merchant payment without traditional correspondent banking

**Code Implementation**:
1. **EU Banking Layer** (`models.py` + `services.py`): Simulates PSD2 open banking with account access and payment initiation
2. **Currency Exchange Engine** (`services.convert_currency()`): Real-time EUR/THB conversion with transparent fee structure
3. **PromptPay Integration** (`services.parse_promptpay_qr()`): Thai payment system connectivity via QR code parsing
4. **Transaction Orchestration** (`services.process_payment()`): End-to-end payment flow coordination
5. **Mobile-First UI**: Touch-optimized interface designed for tourist usage scenarios

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

### Frontend
- ✅ Mobile-responsive UI with 7 pages
- ✅ QR code scanner with camera integration
- ✅ Currency formatting and amount persistence
- ✅ PIN entry system
- ✅ Multi-step payment flow

### Backend
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

## 📈 Scaling Prerequisites & Technological Risks

### Prerequisites for Scale-Out
1. **Database Infrastructure**: Transition from in-memory to distributed PostgreSQL with read replicas
2. **Microservices Architecture**: Separate EU banking, Thai payments, and FX services
3. **API Gateway**: Rate limiting, authentication, and request routing
4. **Message Queues**: Asynchronous transaction processing (Redis/RabbitMQ)
5. **Real Banking Integration**: PSD2 certification and PromptPay partnership agreements
6. **Compliance Infrastructure**: AML/KYC automation and regulatory reporting systems

### Technological Risks
- **Regulatory Changes**: PSD2 Strong Customer Authentication evolution
- **API Dependency**: EU bank API availability and rate limits
- **Currency Volatility**: Real-time FX rate integration stability
- **Cross-Border Latency**: Network delays affecting transaction completion
- **Data Residency**: EU GDPR vs Thai data localization requirements

## 🔧 Operations & Maintenance Challenges

### Development & Deployment
- **Environment Consistency**: Docker containerization for dev/staging/prod parity
- **Database Migrations**: Handling schema changes across distributed systems
- **Third-Party Integration**: Managing EU bank API versioning and Thai payment system updates
- **Monitoring**: Real-time transaction status, fraud detection, and system health

### Operational Challenges
1. **24/7 Availability**: Cross-timezone support for EU-Thailand payment flows
2. **Transaction Reconciliation**: Daily settlement between EU debits and Thai credits
3. **Customer Support**: Multi-language support and dispute resolution
4. **Compliance Reporting**: Automated AML reporting to both EU and Thai authorities
5. **Liquidity Management**: Maintaining sufficient EUR/THB reserves for settlements

### Maintenance Solutions
- **Automated Testing**: CI/CD pipelines with integration tests for banking APIs
- **Blue-Green Deployment**: Zero-downtime updates for critical payment infrastructure
- **Monitoring & Alerting**: Prometheus/Grafana for system metrics and PagerDuty for incidents
- **Documentation**: API documentation and runbooks for operational procedures

## 🔒 Security Risk Assessment

### Operator Security Risks
1. **API Key Management**: Secure storage of banking API credentials
2. **Data Breaches**: Customer financial data protection (PCI DSS compliance)
3. **System Intrusion**: Unauthorized access to payment processing systems
4. **Insider Threats**: Employee access control and audit trails
5. **Third-Party Risk**: Security of EU banking and Thai payment partners

### User Security Risks
1. **Authentication**: Secure login and session management
2. **Transaction Fraud**: Unauthorized payment initiation
3. **Phishing**: Mobile app security and domain verification
4. **Device Security**: Secure storage of payment credentials on mobile devices
5. **Man-in-the-Middle**: HTTPS and certificate pinning for API communications

### Security Mitigation Strategies
- **Encryption**: End-to-end encryption for all financial data transmission
- **Multi-Factor Authentication**: SCA compliance for EU regulations
- **Fraud Detection**: Machine learning models for suspicious transaction patterns
- **Security Audits**: Regular penetration testing and code security reviews
- **Compliance**: SOC 2 Type II, PCI DSS Level 1, and ISO 27001 certifications

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
