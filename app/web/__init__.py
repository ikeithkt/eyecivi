"""
@author: Twu
@file: __init__.py
@desc: 首页视图
"""
from flask import Blueprint, render_template


def create_blueprint_index():
    bp = Blueprint('web', __name__)

    @bp.route('/')
    def index():
        return render_template('index.html')

    @bp.route('/index')
    def index_film():
        return render_template('index_film.html')

    return bp
