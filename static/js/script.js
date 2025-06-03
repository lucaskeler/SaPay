document.addEventListener('DOMContentLoaded', () => {
    
    // scanning logic 

    const startScanButton = document.getElementById('startScanButton');
    const stopButton = document.getElementById('stopButton');
    const html5QrCode = new Html5Qrcode("reader");
    let isScanning = false;
    const responseArea = document.getElementById('responseArea');

    function startScanner(cameraId) {
        html5QrCode.start(
            cameraId,
            { fps: 10, qrbox: { width: 250, height: 250 } },
            (decodedText, decodedResult) => {
                console.log("QR code detected:", decodedText);
                responseArea.textContent = decodedText;
            },
            (errorMessage) => {
                // ignore parse errors
            }
        ).then(() => {
            isScanning = true;
        }).catch(err => {
            console.error("Failed to start scanner:", err);
        });
    }

    function stopScanner() {
        if (!isScanning) return;
        html5QrCode.stop()
            .then(() => html5QrCode.clear())
            .then(() => {
                console.log("Scanner stopped and cleared.");
                isScanning = false;
            })
            .catch(err => console.error("Failed to stop/clear scanner:", err));
    }

    startScanButton.addEventListener('click', () => {
        if (isScanning) {
            console.log("Scanner already running.");
            return;
        }
        Html5Qrcode.getCameras()
            .then(cameras => {
                if (cameras && cameras.length) {
                    startScanner(cameras[1].id);
                } else {
                    console.error("No cameras found.");
                }
            })
            .catch(err => {
                console.error("Error getting cameras:", err);
            });
    });

    if (stopButton) {
        stopButton.addEventListener('click', stopScanner);
    }

    // if (responseArea) {
    //     myButton.addEventListener('click', async () => {
    //         responseArea.textContent = 'Fetching data...';

    //         try {
    //             const response = await fetch('/get-data');
    //             if (!response.ok) {
    //                 throw new Error(`HTTP error! status: ${response.status}`);
    //             }
    //             const data = await response.json();
    //             responseArea.textContent = JSON.stringify(data, null, 2);
    //         } catch (error) {
    //             console.error('Fetch error:', error);
    //             responseArea.textContent = `Error: ${error.message}`;
    //         }
    //     });
    // } else {
    //     console.error('Button or responseArea not found in the DOM');
    // }
});