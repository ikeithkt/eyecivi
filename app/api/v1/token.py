"""
@author: Twu
@file: token.py
@desc: token
"""
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer

from app.forms.api.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    """获取令牌"""
    form = ClientForm().validate_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify_by_email
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data, form.secret.data
    )

    # token 过期时间
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = __generate_token(identity['uid'], form.type.data, identity['scope'], expiration)
    return jsonify({'token': token.decode('ascii')}), 201


def __generate_token(uid, client_type, scope=None, expiration=7200):
    """生成令牌"""
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expiration)
    return s.dumps({'uid': uid, 'type': client_type, 'scope': scope})
