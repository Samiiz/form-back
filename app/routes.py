from flask import (Blueprint, request, jsonify)

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def connect():
    if request.method == 'GET':
        return jsonify({"message": "Success Connect"})
