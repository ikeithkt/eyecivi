"""
@author: Twu
@file: user.py
@desc: 用户相关模型
"""
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, Boolean, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base, db
from app import login_manager
from app.libs.common_func import is_isbn_or_key
from app.spider.douban import DoubanBook
from app.libs.error_code import AuthFailed


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(65), unique=True, nullable=False)
    phone_number = Column(String(15), unique=True)
    nickname = Column(String(25), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    confirmed = Column(Boolean, default=False)
    auth = Column(SmallInteger, default=1)

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

    @staticmethod
    def register_by_email(nickname, email, password):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = email
            user.password = password
            db.session.add(user)

    @staticmethod
    def verify_by_email(email, password):
        """"用于 API 调用"""
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        authority = 'AdminAuthority' if user.auth == 2 else 'UserAuthority'
        return {'uid': user.id, 'authority': authority}

    @classmethod
    def can_save_to_collect(cls, digit, media_type):
        if media_type == 'book':
            if is_isbn_or_key(digit) != 'isbn':
                return False
            douban_book = DoubanBook()
            douban_book.search_by_isbn(digit)
            if not douban_book.first:
                return False
        elif media_type == 'film':
            pass
        return True


@login_manager.user_loader
def get_user(uid):
    """获取当前用户，在 flask_login.login_required 需要"""
    return User.query.get(int(uid))
