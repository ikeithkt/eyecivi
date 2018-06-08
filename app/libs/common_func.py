"""
@author: TuTeng
@file: common_func.py
@desc: 辅助模块
"""


def is_isbn_or_key(word):
    """判断是普通关键字还是 ISBN"""
    isbn_or_key = 'key'  # 普通关键字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'  # ISBN13
    else:
        short_word = word.replace('-', '')
        if '-' in word and len(short_word) == 10 and short_word.isdigit():
            isbn_or_key = 'isbn'  # ISBN10
    return isbn_or_key
