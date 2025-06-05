document.addEventListener('DOMContentLoaded', () => {

    // Loading page logic
    if (window.location.pathname === '/loading') {
        console.log("Loading page detected, starting mock delay...");
        // Mock loading delay - navigate to payment screen after 2.5 seconds
        setTimeout(() => {
            console.log("Navigating to payment screen...");
            window.location.href = "/payment";
        }, 2500); // 2.5 seconds delay
    }
});