"""
@author: Twu
@file: __init__.py
@desc:
"""
from flask import Blueprint
from app.web.user import auth


def create_blueprint_user():
    bp = Blueprint('user', __name__)

    auth.api.register(bp)

    return bp
