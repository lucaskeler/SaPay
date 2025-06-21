document.addEventListener('DOMContentLoaded', () => {

    // Loading page logic
    if (window.location.pathname === '/loading') {
        // Different navigation behaviour if previous page was the pin screen
        if (new URL(document.referrer).pathname === '/pin') {
            console.log("Loading page detected, starting mock delay...");
            // Mock loading delay - navigate to payment screen after 2.5 seconds
            setTimeout(() => {
                console.log("Navigating to success screen...");
                window.location.href = "/success";
            }, 2500); // 2.5 seconds delay
        }

        else {
            console.log("Loading page detected, starting mock delay...");
            // Mock loading delay - navigate to payment screen after 2.5 seconds
            setTimeout(() => {
                console.log("Navigating to payment screen...");
                window.location.href = "/payment";
            }, 2500); // 2.5 seconds delay
        }
    }
});