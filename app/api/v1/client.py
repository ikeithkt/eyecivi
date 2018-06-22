"""
@author: Twu
@file: client.py
@desc:
"""
from flask import jsonify

from app.libs.redprint import Redprint
from app.forms.api.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm()
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_by_email,
            ClientTypeEnum.USER_MOBILE: __register_by_mobile()
        }
        promise[form.type.data]()
    else:
        return jsonify({'msg': 'register failed'})
        # TODO: raise Exception
        pass
    return jsonify({'msg': 'register success'})


def __register_by_email():
    form = UserEmailForm().validate_api()
    User.register_by_email(nickname=form.nickname.data,
                           email=form.account.data,
                           password=form.secret.data)


def __register_by_mobile():
    pass
