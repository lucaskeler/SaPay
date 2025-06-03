import os 
import qrcode 
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')


# API endpoint our JS script calls 
@app.route('/get-data', methods=['GET'])
def get_data():
    sample_data = {
        "message": "Hello from Flask",
        "status": "success",
        "items": ["apple", "banana", "cherry"],
        "timestamp": "Just now"
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
