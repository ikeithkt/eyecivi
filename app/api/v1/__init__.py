"""
@author: Twu
@file: __init__.py
@desc:
"""
from flask import Blueprint

from app.api.v1 import book, client, token, user


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    user.api.register(bp_v1)

    return bp_v1
