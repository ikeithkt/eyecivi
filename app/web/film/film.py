"""
@author: Twu
@file: film.py
@desc:
"""
from flask import render_template, request, flash
from flask_login import current_user

from app.libs.redprint import Redprint
from app.forms.base import SearchForm
from app.models.base import db
from app.models.collection import CollectionFilm
from app.view_models.film import FilmCollection, FilmViewModel
from app.spider.douban import DoubanFilm
from app.models.history import FilmHistory

api = Redprint('film')


@api.route('')
def index():
    histories = FilmHistory.get_film_history()
    films = [FilmViewModel(history.film) for history in histories]
    return render_template('film/film.html', films=films)


@api.route('/search')
def search():
    form = SearchForm(request.args)
    films = FilmCollection()

    if form.validate():
        q = form.q.data
        page = form.page.data

        douban_film = DoubanFilm()
        douban_film.search_by_keyword(q, page)

        films.fill(douban_film, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字！')
    return render_template('film/search_result.html', films=films)


@api.route('/detail/<fid>')
def film_detail(fid):
    is_collect = False

    douban_film = DoubanFilm()
    douban_film.search_by_digits(fid)
    film = FilmViewModel(douban_film.first)

    history = FilmHistory.query.filter_by(fid=fid).first()
    with db.auto_commit():
        if history:
            history.increase()
        else:
            new_history = FilmHistory()
            new_history.fid = fid
            db.session.add(new_history)

    if current_user.is_authenticated:
        if CollectionFilm.query.filter_by(uid=current_user.id, fid=fid).first():
            is_collect = True

    return render_template('film/film_detail.html', film=film, is_collect=is_collect)
