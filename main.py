from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

@app.route('/generate-signature', methods=['POST'])

def generate_signature():
    data = request.get_json()
    path = data.get('path')
    token = data.get('token')

    if not path or not token:
        return jsonify({"error": "Missing path or token"}), 400

    # Match exact Python format
    timestamp = round(time.time() * 1000 - 60)
    raw = fr"{path}\r\n{token}\r\n{timestamp}"
    signature = hashlib.md5(raw.encode('utf-8')).hexdigest().lower()

    return jsonify({
        "signature": signature,
        "timestamp": timestamp
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
