"""
@author: Twu
@file: auth.py
@desc: 用户视图
"""
from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required

from app.libs.redprint import Redprint
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User

api = Redprint('auth')


@api.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attr(form.data)
            db.session.add(user)
        return redirect(url_for('user.login'))
    return render_template('auth/register.html', form=form)


@api.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next_url = request.args.get('nest')
            if not next_url or not next_url.statswith('/'):
                next_url = url_for('web.index')
            return redirect(next_url)
        else:
            flash('账号不存在或密码错误！')
    return render_template('auth/login.html', form=form)


@api.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@api.route('/reset/password')
def forget_password_request():
    pass
