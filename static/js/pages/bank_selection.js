// Bank selection page functionality
// Load EU bank accounts from backend and handle selection

document.addEventListener('DOMContentLoaded', function() {
    const bankList = document.getElementById('bankList');
    
    // Load banks when page loads
    loadBankAccounts();
    
    function loadBankAccounts() {
        // Fetch bank accounts from backend
        fetch('/api/banks')
            .then(response => response.json())
            .then(banks => {
                displayBanks(banks);
            })
            .catch(error => {
                console.log('Error loading banks:', error);
                // Show some default banks if API fails
                showDefaultBanks();
            });
    }
    
    function displayBanks(banks) {
        bankList.innerHTML = '';  // Clear existing content
        
        banks.forEach(function(bank) {
            const bankCard = createBankCard(bank);
            bankList.appendChild(bankCard);
        });
    }
    
    function createBankCard(bank) {
        const card = document.createElement('div');
        card.className = 'card bank-card';
        card.style.cursor = 'pointer';
        card.style.marginBottom = '15px';
        
        // Bank card content
        card.innerHTML = `
            <div class="bank-card-content" style="display: flex; justify-content: space-between; align-items: center; padding: 15px;">
                <div class="bank-info">
                    <h3 style="margin: 0; color: #333;">${bank.bank_name}</h3>
                    <p style="margin: 5px 0; color: #666; font-size: 14px;">${bank.account_holder}</p>
                    <p style="margin: 0; color: #2196F3; font-weight: bold;">€${bank.balance.toFixed(2)}</p>
                </div>
                <div class="bank-arrow" style="font-size: 20px; color: #999;">→</div>
            </div>
        `;
        
        // Add click handler to select bank
        card.addEventListener('click', function() {
            selectBank(bank);
        });
        
        return card;
    }
    
    function selectBank(bank) {
        // Store selected bank in sessionStorage
        sessionStorage.setItem('selectedBank', JSON.stringify(bank));
        
        // Show selection feedback
        console.log('Selected bank:', bank.bank_name);
        
        // Navigate back to home page
        window.location.href = '/';
    }
    
    function showDefaultBanks() {
        // Fallback banks if API doesn't work
        const defaultBanks = [
            {
                account_id: 'DB_001',
                bank_name: 'Deutsche Bank',
                balance: 2847.50,
                currency: 'EUR',
                account_holder: 'Demo User'
            },
            {
                account_id: 'BNP_001',
                bank_name: 'BNP Paribas', 
                balance: 1205.75,
                currency: 'EUR',
                account_holder: 'Demo User'
            }
        ];
        
        displayBanks(defaultBanks);
    }
}); 