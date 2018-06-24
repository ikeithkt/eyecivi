"""
@author: Twu
@file: error_code.py
@desc: API 的返回 error
"""
from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400  # 请求参数错误
    msg = 'client is invalid'
    error_code = 1001


class ClientCreateSuccess(APIException):
    code = 201  # 创建或更新成功
    msg = 'client create success'
    error_code = 0


class DeleteSuccess(APIException):
    code = 202  # 204：删除成功，但 API 不会返回任何内容，所以用 202 代替
    msg = 'delete success'
    error_code = 1


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 2001


class AuthFailed(APIException):
    code = 401  # 未授权
    msg = 'authorization failed'
    error_code = 1002


class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not in authority'
    error_code = 1005
