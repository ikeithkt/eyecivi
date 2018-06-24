"""
@author: Twu
@file: history.py
@desc: 访问详情页历史
"""
from sqlalchemy import Column, Integer, String, desc

from app.models.base import Base
from app.spider.douban import DoubanBook, DoubanFilm


class History(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=1)

    def increase(self):
        self.count += 1


class BookHistory(History):
    isbn = Column(String(15), nullable=False, unique=True)

    @classmethod
    def get_book_history(cls):
        history = BookHistory.query.filter_by().order_by(desc(cls.count)).all()
        return history

    @property
    def book(self):
        douban_book = DoubanBook()
        douban_book.search_by_isbn(self.isbn)
        return douban_book.first


class FilmHistory(History):
    fid = Column(String(15), nullable=False, unique=True)

    @classmethod
    def get_film_history(cls):
        history = FilmHistory.query.filter_by().order_by(desc(cls.count)).all()
        return history

    @property
    def film(self):
        douban_film = DoubanFilm()
        douban_film.search_by_digits(self.fid)
        return douban_film.first
