"""
@author: TuTeng
@file: book.py
@desc:
"""
from flask import request, jsonify

from app.web import web
from app.libs.common_func import is_isbn_or_key
from app.spider.douban_book import DoubanBook


@web.route('/book/search')
def search():
    q = request.args.get('q')
    page = request.args.get('page')
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = DoubanBook.search_by_isbn(q)
    else:
        result = DoubanBook.search_by_keyword(q, page)
    return jsonify(result)
