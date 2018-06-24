"""
@author: Twu
@file: collection.py
@desc:
"""
from sqlalchemy import Integer, ForeignKey, Column, String, desc
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.spider.douban import DoubanBook, DoubanFilm


class CollectionBook(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)

    @classmethod
    def get_my_collection(cls, uid):
        collection = CollectionBook.query.filter_by(uid=uid).order_by(desc(CollectionBook.create_time)).all()
        return collection

    @property
    def book(self):
        douban_book = DoubanBook()
        douban_book.search_by_isbn(self.isbn)
        return douban_book.first


class CollectionFilm(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    fid = Column(String(15), nullable=False)

    @classmethod
    def get_my_collection(cls, uid):
        collection = CollectionFilm.query.filter_by(uid=uid).order_by(desc(CollectionFilm.create_time)).all()
        return collection

    @property
    def film(self):
        douban_film = DoubanFilm()
        douban_film.search_by_digits(self.fid)
        return douban_film.first
