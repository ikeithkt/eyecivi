"""
@author: Twu
@file: user.py
@desc: 用户信息
"""
from flask_login import login_required
from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('user')


# @api.route('/user/<int:uid>')
# @login_required
# def get_user(uid):
#     user = User.query.get_or_404(uid)
#     return dict(user)
