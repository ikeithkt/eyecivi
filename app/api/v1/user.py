"""
@author: Twu
@file: user.py
@desc:
"""
from app.libs.redprint import Redprint
from app.libs.token_require import auth

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    pass

