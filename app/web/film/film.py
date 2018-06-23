"""
@author: Twu
@file: film.py
@desc:
"""
from flask import render_template, request, flash

from app.libs.redprint import Redprint
from app.forms.base import SearchForm
from app.view_models.film import FilmSingle, FilmCollection, FilmViewModel
from app.spider.douban import DoubanFilm

api = Redprint('film')


@api.route('')
def index():
    return render_template('film/film.html')


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
    douban_film = DoubanFilm()
    douban_film.search_by_digits(fid)
    film = FilmViewModel(douban_film.first)

    return render_template('film/film_detail.html', film=film)
