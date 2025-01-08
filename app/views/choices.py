from flask import request

from app.models import Choices
from config import db


def create_choices():
    data = request.get_json()
    choice = Choices(
        content=data["content"],
        sqe=data["sqe"],
        question_id=data["question_id"],
    )

    db.session.add(choice)
    db.session.commit()

    return choice


def get_choice_by_id(choice_id):
    choice = Choices.query.filter_by(id=choice_id).first()
    return choice


def get_choices_sort_sqe(qusetion_id):
    choices = (
        Choices.query.filter_by(is_active=True, question_id=qusetion_id)
        .order_by(Choices.sqe)
        .all()
    )
    return [choice.to_dict() for choice in choices]
