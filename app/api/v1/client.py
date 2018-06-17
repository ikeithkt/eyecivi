"""
@author: Twu
@file: client.py
@desc:
"""
from flask import jsonify

from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('/register', methods=['POSt'])
def create_client():
    return jsonify({'msg': 'ok'})
