"""
@author: TuTeng
@file: douban.py
@desc: 豆瓣图书 API
"""
from flask import current_app

from app.libs.httper import HTTP


class Douban:
    __abstract__ = True

    def __init__(self):
        self.total = 0
        self.media = []

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.media[0] if self.total > 0 else None


class DoubanBook(Douban):
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fit_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                      self.calculate_start(page))
        result = HTTP.get(url)
        self.__fit_collection(result)

    def __fit_single(self, data):
        if data:
            self.total = 1
            self.media.append(data)

    def __fit_collection(self, data):
        if data:
            self.total = data['total']
            self.media = data['books']


class DoubanFilm(Douban):
    id_url = 'https://api.douban.com/v2/movie/subject/{}'
    keyword_url = 'https://api.douban.com/v2/movie/search?q={}&count={}&start={}'

    def search_by_digits(self, digits):
        url = self.id_url.format(digits)
        result = HTTP.get(url)
        self.__fit_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                      self.calculate_start(page))
        result = HTTP.get(url)
        self.__fit_collection(result)

    def __fit_single(self, data):
        if data:
            self.total = 1
            self.media.append(data)

    def __fit_collection(self, data):
        if data:
            self.total = data['total']
            self.media = data['subjects']
