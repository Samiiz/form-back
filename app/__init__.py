from flask import Flask, request, jsonify
from flask_migrate import Migrate
import requests

import app.models
from config import db

migrate = Migrate()

from app.routes import routes

HTTP_SERVER_URL = "http://3.38.247.83:3000"

def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

    # 블루 프린트 등록
    application.register_blueprint(routes)
    @routes.route('/proxy/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy(path):
        """
        HTTP 서버로 요청을 전달하고 응답을 반환하는 프록시.
        """
        # HTTP 서버 URL
        url = f"{HTTP_SERVER_URL}/{path}"

        try:
            # HTTP 요청 전송
            response = requests.request(
                method=request.method,
                url=url,
                headers={key: value for key, value in request.headers if key != 'Host'},
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False
            )

            # HTTP 응답 반환
            return response.content, response.status_code, response.headers.items()

        except requests.exceptions.RequestException as e:
            # 요청 실패 시 에러 반환
            return jsonify({"error": f"HTTP 요청 실패: {str(e)}"}), 500

    return application