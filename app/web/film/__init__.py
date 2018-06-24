"""
@author: Twu
@file: __init__.py
@desc:
"""
from flask import Blueprint

from app.web.film import film, collect


def create_blueprint_film():
    bp = Blueprint('film', __name__)

    film.api.register(bp)
    collect.api.register(bp)

    return bp
