"""
@author: Twu
@file: film.py
@desc:
"""
import re


class FilmSingle:
    def __init__(self, film):
        self.rating = film['rating']['average']
        self.genres = '/'.join(film['genres'])
        self.title = film['title']
        self.casts = '/'.join([cast['name'] for cast in film['casts']])
        self.original_title = film['original_title']
        self.directors = '/'.join(director['name'] for director in film['directors'])
        self.year = film['year']
        self.image = self.__get_image(film['images']['small'])
        self.id = film['id']

    @staticmethod
    def __get_image(image_url):
        url = 'https://img1.doubanio.com/lpic/{}.jpg'
        sid = re.search(r's\d+', image_url)
        if sid:
            return url.format(sid.group())
        return image_url

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.original_title, self.genres, self.year])
        return '/'.join(intros)

    @property
    def intro_people(self):
        intro_people = filter(lambda x: True if x else False,
                              [self.directors, self.casts])
        return '/'.join(intro_people)


class FilmCollection:
    def __init__(self):
        self.keyword = ''
        self.total = 0
        self.films = []

    def fill(self, films, key):
        self.keyword = key
        self.total = films.total
        self.films = [FilmSingle(film) for film in films.media]


class FilmViewModel(FilmSingle):
    def __init__(self, film):
        super().__init__(film)
        self.countries = '/'.join(film['countries'])
        self.summary = film['summary']
