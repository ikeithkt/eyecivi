"""
@author: TuTeng
@file: douban_book.py
@desc: 豆瓣图书 API
"""
from flask import current_app

from app.libs.httper import HTTP


class DoubanBook:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fit_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                      self.calculate_start(page))
        result = HTTP.get(url)
        self.__fit_collection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

    def __fit_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fit_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    @property
    def first(self):
        return self.books[0] if self.total > 0 else None
