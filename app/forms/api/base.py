"""
@author: Twu
@file: base.py
@desc: api Form 基类
"""
from wtforms import Form
from wtforms.validators import ValidationError
from flask import request


class Base(Form):
    def __init__(self):
        """实例化 Form 时就获取请求中的数据"""
        data = request.get_json(silent=True)
        args = request.args.to_dict()

        super().__init__(data=data, **args)

    def validate_api(self):
        """自定义一个api的验证"""
        valid = super().validate()
        if not valid:
            ValidationError()
        return self
