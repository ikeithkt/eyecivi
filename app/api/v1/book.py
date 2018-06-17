"""
@author: Twu
@file: book.py
@desc: api book
"""
from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/search')
def search():
    pass
