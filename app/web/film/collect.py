"""
@author: Twu
@file: collection.py
@desc:
"""
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.libs.redprint import Redprint
from app.models.base import db
from app.models.collection import CollectionFilm
from app.view_models.film import FilmViewModel

api = Redprint('collect')


@api.route('/film/my')
@login_required
def my_collect():
    uid = current_user.id
    collection = CollectionFilm.get_my_collection(uid)
    films = [FilmViewModel(col.film) for col in collection]
    return render_template('film/my_collection.html', films=films)


@api.route('film/<fid>')
@login_required
def save_to_collect(fid):
    if current_user.can_save_to_collect(fid, 'film'):
        with db.auto_commit():
            col = CollectionFilm()
            col.fid = fid
            col.uid = current_user.id
            db.session.add(col)
    else:
        flash('这部电影已经被您收藏了，请不要重复收藏！')
    return redirect(url_for('film.film_detail', fid=fid))


@api.route('film/cancel/<fid>')
@login_required
def cancel_from_collect(fid):
    col = CollectionFilm.query.filter_by(fid=fid).first_or_404()
    with db.auto_commit():
        col.delete()
    return redirect(url_for('film.my_collect'))
