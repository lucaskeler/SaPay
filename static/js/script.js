document.addEventListener('DOMContentLoaded', () => {
    
    // scanning logic 

    const startScanButton = document.getElementById('startScanButton');
    const stopButton = document.getElementById('stopButton');
    const readerElement = document.getElementById('reader');
    const html5QrCode = new Html5Qrcode("reader");
    let isScanning = false;
    // const responseArea = document.getElementById('responseArea');

    function startScanner(cameraId) {
        html5QrCode.start(
            cameraId,
            {
                fps: 60,    // fames per second
                qrbox: function(viewfinderWidth, viewfinderHeight) {
                    // Make the qrbox responsive and properly sized
                    let minEdgePercentage = 0.6; // 60% of the smaller dimension to ensure it fits well within video
                    let minEdgeSize = Math.min(viewfinderWidth, viewfinderHeight);
                    let qrboxSize = Math.floor(minEdgeSize * minEdgePercentage);
                    return {
                        width: qrboxSize,
                        height: qrboxSize
                    };
                },
                // aditional viewfinder configurations
                aspectRatio: 1.0,           // square viewfinder for better alignment
                disableFlip: false,         // allow horizontal flip
                videoConstraints: {         // camera quality settings
                    width: { min: 480, ideal: 640, max: 1080 },
                    height: { min: 480, ideal: 640, max: 1080 },
                    facingMode: "environment"  // use back camera
                }
            },
            (decodedText, decodedResult) => {
                console.log("QR code detected:", decodedText);
                // trigger next screen regardless of the QR code content
                window.location.href = "/loading"; 
            },
            (errorMessage) => {
                // ignore parse errors, just keep scanning
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
});