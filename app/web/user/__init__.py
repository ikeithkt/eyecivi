"""
@author: Twu
@file: __init__.py
@desc:
"""
from flask import Blueprint
from app.web.user import auth


def create_blueprint_user():
    bp_user = Blueprint('user', __name__)

    auth.api.register(bp_user)

    return bp_user
