from flask import jsonify, request, session

from app.models import Answer
from config import db


def create_answer():
    data = request.get_json()
    answer = Answer(
        user_id=data["user_id"],
        choice_id=data["choice_id"],
    )
    db.session.add(answer)
    db.session.commit()
    return jsonify({"message": f"{data["user_id"]}'s Answer created"})


def create_answers():
    data = request.json

    answers_list = data.get("answers", [])

    for answer_data in answers_list:
        choice_id = answer_data["choice_id"]
        answer = Answer(
            user_id=session.get("user_id"), choice_id=choice_id
        )
        db.session.add(answer)

    db.session.commit()

    return jsonify({"message": "모든 답변이 저장되었습니다."}), 200
