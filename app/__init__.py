"""
@author: TuTeng
@file: __init__.py.py
@desc: 创建 app
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import create_blueprint_book
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_book())
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    pass
