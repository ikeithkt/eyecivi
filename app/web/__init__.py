"""
@author: TuTeng
@file: __init__.py.py
@desc:
"""
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
