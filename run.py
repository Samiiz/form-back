from app import create_app
from flask_cors import CORS  # CORS 임포트

app = create_app()
CORS(app)  # CORS 설정 (모든 출처에서의 요청 허용)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # 로컬 네트워크에서 접근 가능하도록 설정
