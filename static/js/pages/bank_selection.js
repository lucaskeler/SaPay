// EU bank selection functionality
// simulates PSD2 open banking connection

// mock EU bank accounts data
const euBanks = [
    {
        id: 'deutsche_bank',
        name: 'Deutsche Bank',
        country: 'Germany',
        iban: 'DE89 3704 0044 0532 0130 00',
        balance: 2847.50,
        currency: 'EUR',
        logo: '🏦'
    },
    {
        id: 'bnp_paribas',
        name: 'BNP Paribas',
        country: 'France', 
        iban: 'FR14 2004 1010 0505 0001 3M02 606',
        balance: 1205.75,
        currency: 'EUR',
        logo: '🏛️'
    },
    {
        id: 'ing_bank',
        name: 'ING Bank',
        country: 'Netherlands',
        iban: 'NL91 ABNA 0417 1643 00',
        balance: 3156.20,
        currency: 'EUR',
        logo: '🧡'
    }
];

// create bank selection cards using HTML template
function createBankCard(bank) {
    const template = document.getElementById('bankCardTemplate');
    const clone = template.content.cloneNode(true);
    
    // populate template with bank data
    clone.querySelector('.bank-card').setAttribute('data-bank-id', bank.id);
    clone.querySelector('.bank-logo').textContent = bank.logo;
    clone.querySelector('.bank-name').textContent = bank.name;
    clone.querySelector('.bank-country').textContent = bank.country;
    clone.querySelector('.bank-balance').textContent = `€${bank.balance.toLocaleString('en-US', {minimumFractionDigits: 2})}`;
    
    return clone;
}

// handle bank selection
function selectBank(bankId) {
    const selectedBank = euBanks.find(bank => bank.id === bankId);
    if (selectedBank) {
        // store selected bank in sessionStorage
        sessionStorage.setItem('selectedBank', JSON.stringify(selectedBank));
        console.log('Selected bank:', selectedBank.name);
        
        // navigate to home page 
        window.location.href = '/';
    }
}

// initialize bank selection page
document.addEventListener('DOMContentLoaded', function() {
    const bankList = document.getElementById('bankList');
    
    if (bankList) {
        // populate bank list using templates
        euBanks.forEach(bank => {
            const bankCard = createBankCard(bank);
            bankList.appendChild(bankCard);
        });
        
        // add click listeners to bank cards
        document.querySelectorAll('.bank-card').forEach(card => {
            card.addEventListener('click', function() {
                const bankId = this.getAttribute('data-bank-id');
                selectBank(bankId);
            });
        });
    }
}); 