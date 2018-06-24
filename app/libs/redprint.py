"""
@author: Twu
@file: redprint.py
@desc: 红图
"""


class Redprint:
    def __init__(self, name):
        """
        :param name: 红图名字
        """
        self.name = name
        self.mound = []

    def register(self, bp, url_prefix=None):
        if not url_prefix:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator
