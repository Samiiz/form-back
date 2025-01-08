from app import create_app
from flask import Flask, jsonify
from flask_cors import CORS  # CORS 임포트

app = create_app()
CORS(app)  # CORS 설정 (모든 출처에서의 요청 허용)

@app.route('', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from your local Flask server!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # 로컬 네트워크에서 접근 가능하도록 설정
