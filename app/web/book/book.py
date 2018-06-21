"""
@author: Twu
@file: book.py
@desc: 书籍视图
"""
import json

from flask import request

from app.libs.redprint import Redprint
from app.libs.common_func import is_isbn_or_key
from app.spider.douban_book import DoubanBook
from app.view_models.book import BookCollection

api = Redprint('book')


@api.route('/search')
def search():
    q = request.args.get('q')
    page = int(request.args.get('page'))
    isbn_or_key = is_isbn_or_key(q)

    douban_book = DoubanBook()
    books = BookCollection()
    if isbn_or_key == 'isbn':
        douban_book.search_by_isbn(q)
    else:
        douban_book.search_by_keyword(q, page)

    books.fill(douban_book, q)
    return json.dumps(books, default=lambda o: o.__dict__)
