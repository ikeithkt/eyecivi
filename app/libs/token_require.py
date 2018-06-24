"""
@author: Twu
@file: token_require.py
@desc: token 相关
"""
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.authority import is_in_authority

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'client_type', 'authority'])


@auth.verify_password
def http_token(token, password):
    """利用 HTTPBasicAuth 中的 verify_password 获取token"""
    user_info = __verity_token(token)
    if not user_info:
        return False
    g.user = user_info
    return True


def __verity_token(token):
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1003)
    except SignatureExpired:
        raise AuthFailed(msg='token is expiration', error_code=1004)

    uid = data['uid']
    client_type = data['type']
    authority = data['authority']

    if not is_in_authority(authority, request.endpoint):
        raise Forbidden()

    return User(uid, client_type, authority)
