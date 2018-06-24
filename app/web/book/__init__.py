"""
@author: Twu
@file: __init__.py
@desc:
"""
from flask import Blueprint

from app.web.book import book, collect


def create_blueprint_book():
    bp = Blueprint('book', __name__)

    book.api.register(bp)
    collect.api.register(bp)

    return bp
