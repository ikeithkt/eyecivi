"""
@author: Twu
@file: __init__.py
@desc: 首页视图
"""
from flask import Blueprint, render_template


def create_blueprint_index():
    bp_index = Blueprint('web', __name__)

    @bp_index.route('/')
    def index():
        return render_template('index.html')

    return bp_index
