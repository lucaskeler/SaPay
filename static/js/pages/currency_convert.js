// Currency formatting and amount persistence across pages
// handles the connection between payment input and success display

// store the input elements
const payAmount = document.querySelector('#amountField');
const payAmountDisplay = document.getElementById('displayField');

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

    // Add event listener to store amount in sessionStorage when input changes
    payAmount.addEventListener('input', function() {
        const rawValue = inputAmount.getRawValue();
        sessionStorage.setItem('paymentAmount', rawValue);
    });

    // Load previously stored amount if it exists
    const storedAmount = sessionStorage.getItem('paymentAmount');
    if (storedAmount) {
        inputAmount.setRawValue(storedAmount);
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