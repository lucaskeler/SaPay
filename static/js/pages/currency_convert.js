// Currency formatting and amount persistence across pages
// handles the connection between payment input and success display
// includes EU currency conversion

// store the input elements
const payAmount = document.querySelector('#amountField');
const payAmountDisplay = document.getElementById('displayField');
const conversionDisplay = document.getElementById('conversionDisplay');

// mock exchange rate - in real app this would come from API
const EXCHANGE_RATE = 38.45; // EUR to THB

// update conversion display when amount changes
function updateConversionDisplay(thbAmount) {
    if (!conversionDisplay) return;
    
    // clear previous content
    conversionDisplay.innerHTML = '';
    
    if (thbAmount && thbAmount > 0) {
        const template = document.getElementById('conversionTemplate');
        if (template) {
            const clone = template.content.cloneNode(true);
            
            // populate template with conversion data
            const eurAmount = (thbAmount / EXCHANGE_RATE).toFixed(2);
            clone.querySelector('.eur-amount').textContent = `€${eurAmount}`;
            clone.querySelector('.exchange-rate').textContent = `Rate: ${EXCHANGE_RATE.toFixed(2)} THB/EUR`;
            
            conversionDisplay.appendChild(clone);
        }
    }
}

// Only initialize if elements exist on current page
if (payAmount) {
    // currency conversion for filled in amount
    const inputAmount = new Cleave('#amountField', {
        numeral: true,
        numeralThousandsGroupStyle: 'thousand',
        numeralDecimalMark: '.',
        numeralDecimalScale: 2,
        prefix: '฿ ',
        rawValueTrimPrefix: true
    });

    // Add event listener to store amount and update conversion display
    payAmount.addEventListener('input', function() {
        const rawValue = inputAmount.getRawValue();
        sessionStorage.setItem('paymentAmount', rawValue);
        updateConversionDisplay(parseFloat(rawValue));
    });

    // Load previously stored amount if it exists
    const storedAmount = sessionStorage.getItem('paymentAmount');
    if (storedAmount) {
        inputAmount.setRawValue(storedAmount);
        updateConversionDisplay(parseFloat(storedAmount));
    }
}

if (payAmountDisplay) {
    // Load amount from sessionStorage and display it
    const storedAmount = sessionStorage.getItem('paymentAmount');
    if (storedAmount && storedAmount !== '0') {
        // Format the number manually since displayField is a div, not an input
        const numericValue = parseFloat(storedAmount);
        const formattedAmount = '฿ ' + numericValue.toLocaleString('en-US', {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
        payAmountDisplay.textContent = formattedAmount;
    } else {
        payAmountDisplay.textContent = '฿ 0.00';
    }
}