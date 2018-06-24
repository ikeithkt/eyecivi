"""
@author: Twu
@file: collection.py
@desc:
"""
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.libs.redprint import Redprint
from app.models.base import db
from app.models.collection import CollectionBook
from app.view_models.book import BookSingle

api = Redprint('collect')


@api.route('/book/my')
@login_required
def my_collect():
    uid = current_user.id
    collection = CollectionBook.get_my_collection(uid)
    books = [BookSingle(col.book) for col in collection]
    return render_template('book/my_collection.html', books=books)


@api.route('book/<isbn>')
@login_required
def save_to_collect(isbn):
    if current_user.can_save_to_collect(isbn, 'book'):
        with db.auto_commit():
            col = CollectionBook()
            col.isbn = isbn
            col.uid = current_user.id
            db.session.add(col)
    else:
        flash('这本书已经被您收藏了，请不要重复收藏！')
    return redirect(url_for('book.book_detail', isbn=isbn))


@api.route('book/cancel/<isbn>')
@login_required
def cancel_from_collect(isbn):
    col = CollectionBook.query.filter_by(isbn=isbn).first_or_404()
    with db.auto_commit():
        col.delete()
    return redirect(url_for('book.my_collect'))
