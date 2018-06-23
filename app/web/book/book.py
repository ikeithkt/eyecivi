"""
@author: Twu
@file: book.py
@desc: 书籍视图
"""
from flask import request, flash, render_template

from app.forms.book import SearchForm
from app.libs.redprint import Redprint
from app.libs.common_func import is_isbn_or_key
from app.spider.douban_book import DoubanBook
from app.view_models.book import BookCollection, BookSingle

api = Redprint('book')


@api.route('')
def index():
    return render_template('book/book.html')


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
    doubanbook = DoubanBook()
    doubanbook.search_by_isbn(isbn)
    book = BookSingle(doubanbook.first)

    return render_template('book/book_detail.html', book=book)
