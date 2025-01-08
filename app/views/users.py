from flask import jsonify, request

from app.models import User
from config import db


def create_user():
    data = request.get_json()

    user = User(
        name=data["name"], age=data["age"], gender=data["gender"], email=data["email"]
    )

    db.session.add(user)
    db.session.commit()
    return user