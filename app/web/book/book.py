"""
@author: Twu
@file: book.py
@desc: 书籍视图
"""
from flask import request, flash, render_template
from flask_login import current_user

from app.forms.base import SearchForm
from app.libs.redprint import Redprint
from app.libs.common_func import is_isbn_or_key
from app.models.base import db
from app.models.history import BookHistory
from app.spider.douban import DoubanBook
from app.view_models.book import BookCollection, BookSingle
from app.models.collection import CollectionBook

api = Redprint('book')


@api.route('')
def index():
    histories = BookHistory.get_book_history()
    books = [BookSingle(history.book) for history in histories]
    return render_template('book/book.html', books=books)


@api.route('/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        douban_book = DoubanBook()
        if isbn_or_key == 'isbn':
            douban_book.search_by_isbn(q)
        else:
            douban_book.search_by_keyword(q, page)

        books.fill(douban_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字！')
    return render_template('book/search_result.html', books=books)


@api.route('/detail/<isbn>')
def book_detail(isbn):
    is_collect = False

    doubanbook = DoubanBook()
    doubanbook.search_by_isbn(isbn)
    book = BookSingle(doubanbook.first)

    history = BookHistory.query.filter_by(isbn=isbn).first()
    with db.auto_commit():
        if history:
            history.increase()
        else:
            new_history = BookHistory()
            new_history.isbn = book.isbn
            db.session.add(new_history)

    if current_user.is_authenticated:
        if CollectionBook.query.filter_by(uid=current_user.id, isbn=isbn).first():
            is_collect = True

    return render_template('book/book_detail.html', book=book, is_collect=is_collect)
