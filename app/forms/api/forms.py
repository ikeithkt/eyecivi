"""
@author: Twu
@file: forms.py
@desc: api Form
"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.forms.api.base import Base as Form
from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='不允许为空'),
                                      Length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, field):
        try:
            client = ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[DataRequired(message='电子邮箱不能为空！'),
                                      Length(8, 64), Email('电子邮箱不符合规范！')])
    secret = StringField(validators=[DataRequired(message='密码不能为空！'),
                                     Length(6, 32)])
    nickname = StringField(validators=[DataRequired(),
                                       Length(2, 10, message='昵称最多2个字符，最多10个字符！')])

    def validate_account(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')