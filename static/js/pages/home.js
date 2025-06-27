// Home page functionality
// Display selected bank information and handle card status

document.addEventListener('DOMContentLoaded', function() {
    const cardStatus = document.getElementById('cardStatus');
    
    // Load selected bank from sessionStorage and display it
    updateSelectedBankDisplay();
    
    function updateSelectedBankDisplay() {
        const selectedBank = sessionStorage.getItem('selectedBank');
        
        if (selectedBank && selectedBank !== 'null') {
            const bank = JSON.parse(selectedBank);
            
            // Update the card status to show selected bank
            if (cardStatus) {
                cardStatus.textContent = `${bank.bank_name} - €${bank.balance.toFixed(2)}`;
                cardStatus.style.color = '#2196F3';
                cardStatus.style.fontWeight = 'bold';
            }
            
            console.log('Loaded selected bank:', bank.bank_name);
        } else {
            // Show default text if no bank is selected
            if (cardStatus) {
                cardStatus.textContent = 'No Bank Selected';
                cardStatus.style.color = '#999';
                cardStatus.style.fontWeight = 'normal';
            }
        }
    }
    
    // Update display when returning from bank selection
    window.addEventListener('focus', function() {
        updateSelectedBankDisplay();
    });
}); 