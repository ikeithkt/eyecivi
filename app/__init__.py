"""
@author: Twu
@file: __init__.py
@desc: 创建 app
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprint(app)
    register_plugin(app)
    return app


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1

    from app.web import create_blueprint_index
    from app.web.book import create_blueprint_book
    from app.web.user import create_blueprint_user

    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

    app.register_blueprint(create_blueprint_index())
    app.register_blueprint(create_blueprint_book())
    app.register_blueprint(create_blueprint_user())


def register_plugin(app):
    from app.models.base import db
    db.init_app(app=app)
    with app.app_context():
        db.create_all()
