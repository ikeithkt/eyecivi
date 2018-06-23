"""
@author: Twu
@file: base.py
@desc: 模型初始化工作和基类
"""
from datetime import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'is_valid' not in kwargs.keys():
            kwargs['is_valid'] = 1
        return super().filter_by(**kwargs)

    def first_or_404(self):
        rv = self.first()
        if not rv:
            # TODO: raise Exception
            pass
        return rv

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            # TODO: raise Exception
            pass
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    is_valid = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attr(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.is_valid = 0
