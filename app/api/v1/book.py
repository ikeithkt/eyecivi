"""
@author: Twu
@file: book.py
@desc: api book
"""
from flask import jsonify, request
from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/search')
def search():
    return jsonify({'msg': 'ok'})
