"""
@author: Twu
@file: user.py
@desc: 用户相关模型
"""
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(65), unique=True, nullable=False)
    phone_number = Column(String(15), unique=True)
    nickname = Column(String(25), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    confirmed = Column(Boolean, default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self.password:
            return False
        return check_password_hash(self.password, raw)
