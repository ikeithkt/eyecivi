"""
@author: Twu
@file: history.py
@desc: 访问详情页历史
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class History(Base):
    id = Column(Integer, primary_key=True)
    # user = relationship('User')
    # uid = Column(Integer, ForeignKey('user.id'))
    count = Column(Integer, default=1)

    def increase(self):
        self.count += 1


class BookHistory(History):
    isbn = Column(String(15), nullable=False, unique=True)
