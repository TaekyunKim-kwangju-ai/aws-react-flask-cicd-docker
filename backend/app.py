# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 도메인에서의 요청을 허용

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(debug=True)
