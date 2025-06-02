// wait for DOM (HTML) to load before running JS code
document.addEventListener('DOMContentLoaded', () => {
    // get the button and response area from the HTML
    const myButton = document.getElementById('myButton');
    const responseArea = document.getElementById('responseArea');

    // check if the button and response area exist
    if (myButton && responseArea) {
        // async so webpage does not freeze while waiting for response
        myButton.addEventListener('click', async () => {
            // provide feedback to user
            responseArea.textContent = 'Fetching data...';

            try {
                // make a request to Flask endpoint '/get-data'
                const response = await fetch('/get-data');

                if (!response.ok) {
                    throw new Error('HTTP error! status: ${response.status}');
                }

                const data = await response.json();
                responseArea.textContent = JSON.stringify(data, null, 2);
            } catch (error) {
                console.error('Fetch error:', error);
                responseArea.textContent = 'Error: ${error.message}';
            }
        });
    } else {
        console.error('Button or responseArea not found in the DOM');
    }
});