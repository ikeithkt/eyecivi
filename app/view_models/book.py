"""
@author: Twu
@file: book.py
@desc: book info
"""


class BookSingle:
    def __init__(self, book):
        self.rating = book['rating']['average']
        self.author = '、'.join(book['author'])
        self.pubdate = book['pubdate']
        self.image = book['image']
        self.binding = book['binding']
        self.pages = book['pages']
        self.publisher = book['publisher']
        self.isbn = book['isbn13']
        self.title = book['title']
        self.price = book['price']
        self.summary = book['summary']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.keyword = ''
        self.total = 0
        self.books = []

    def fill(self, books, key):
        self.keyword = key
        self.total = books.total
        self.books = [BookSingle(book) for book in books.books]
