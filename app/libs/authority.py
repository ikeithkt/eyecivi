"""
@author: Twu
@file: authority.py
@desc: 对视图访问具有的权限
"""


class Authority:
    allow_api = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        return self


class AdminAuthority(Authority):
    pass


class UserAuthority(Authority):
    pass


def is_in_authority(authority, endpoint):
    authority = globals()[authority]()  # 映射到类上并实例化
    return True
