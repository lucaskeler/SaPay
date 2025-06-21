# SaPay - Mobile Payment Processing App

SaPay is a modern web-based payment processing application built with Flask, featuring QR code scanning, secure PIN entry, and real-time amount processing.

## Features

- **QR Code Scanner**: Real-time camera-based QR code detection using the device's back camera
- **Amount Entry**: Interactive currency input with live formatting and validation
- **PIN Security**: Secure 4-digit PIN entry system with visual feedback
- **Payment Flow**: Smooth multi-step transaction process with loading transitions
- **Mobile Responsive**: Optimized for mobile devices with touch-friendly interface
- **Modern UI**: Clean, professional design with custom CSS animations and effects

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Libraries**: 
  - Html5-QRCode for camera scanning
  - Cleave.js for currency formatting
  - Custom responsive CSS framework
- **Security**: SSL/HTTPS enabled for camera access

## Project Structure

```
SaPay/
│
├── app.py                 # Main Flask application with routes
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Home/dashboard page
│   ├── scanner.html      # QR scanner interface
│   ├── loading.html      # Loading transition page
│   ├── payment.html      # Amount entry page
│   ├── pin.html          # PIN entry page
│   └── success.html      # Payment confirmation page
│
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Main stylesheet with responsive design
│   ├── js/
│   │   ├── script.js     # QR scanner logic and camera controls
│   │   └── pages/        # Page-specific JavaScript
│   │       ├── currency_convert.js  # Amount formatting and storage
│   │       ├── pin.js               # PIN entry functionality
│   │       └── timer.js             # Loading page transitions
│   └── img/              # Image assets
│
└── venv/                 # Virtual environment (excluded from git)
```

## Payment Flow

1. **Home** (`/`) - Main dashboard with navigation options
2. **Scanner** (`/scanner`) - QR code scanning interface
3. **Loading** (`/loading`) - Transition page with processing animation
4. **Payment** (`/payment`) - Amount entry with live currency formatting
5. **PIN** (`/pin`) - Secure 4-digit PIN verification
6. **Loading** (`/loading`) - Final processing step
7. **Success** (`/success`) - Payment confirmation with amount display

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SaPay
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the app**
   - Open browser to `https://localhost:5001`
   - Accept SSL certificate warning (self-signed cert for HTTPS camera access)

## Key Features Explained

### QR Scanner
- Uses device's back camera for optimal scanning
- Responsive viewfinder that adapts to screen size
- Real-time detection with visual feedback
- Automatically proceeds to next step on successful scan

### Amount Processing
- Live currency formatting as you type (฿ symbol, thousands separators)
- Amount persistence across page navigation using sessionStorage
- Input validation and formatting using Cleave.js
- Responsive display field with centered text

### PIN Security
- Visual feedback with asterisk masking
- Automatic navigation after 4-digit entry
- Touch-friendly circular buttons
- Mock authentication for demo purposes

### Responsive Design
- Mobile-first approach with touch optimization
- Flexible layouts that work on all screen sizes
- Custom CSS with modern gradients and animations
- Accessibility considerations for all users

## Development Notes

The app uses sessionStorage to maintain payment amount across page transitions, ensuring data persistence during the multi-step payment flow. The QR scanner requires HTTPS to access camera functionality, which is why the Flask app runs with SSL context.

All JavaScript is modular and page-specific, with shared functionality in the main script.js file. The CSS uses CSS custom properties (variables) for consistent theming and easy customization. 