"""
@author: TuTeng
@file: __init__.py.py
@desc:
"""
from flask import Blueprint

from app.web.book import book


def create_blueprint_book():
    bp_web = Blueprint('book', __name__)

    book.api.register(bp_web)

    return bp_web
