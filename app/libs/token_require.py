"""
@author: Twu
@file: token_require.py
@desc: token 相关
"""
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'client_type', 'scope'])


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
    except Exception as e:
        # TODO: raise Exception
        raise e
    uid = data['uid']
    client_type = data['type']
    scope = data['scope']

    return User(uid, client_type, scope)
