"""
@author: Twu
@file: client.py
@desc:
"""
from flask import g

from app.libs.redprint import Redprint
from app.forms.api.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.token_require import auth
from app.models.base import db
from app.models.user import User
from app.libs.error_code import ClientTypeError, ClientCreateSuccess, DeleteSuccess

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm()
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_by_email,
            ClientTypeEnum.USER_MOBILE: __register_by_mobile,
        }
        promise[form.type.data]()
    else:
        raise ClientTypeError()
    return ClientCreateSuccess()


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_client():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


def __register_by_email():
    form = UserEmailForm().validate_api()
    User.register_by_email(nickname=form.nickname.data,
                           email=form.account.data,
                           password=form.secret.data)


def __register_by_mobile():
    pass
