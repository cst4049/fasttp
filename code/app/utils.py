from functools import wraps
from enum import Enum


class ResponseCode(Enum):
    """响应码"""
    Success = 0
    Faild = -1
    Unknow = -2


class InterCode(Enum):
    """内部响应码"""
    pass


def make_response(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            code, msg, data = func(*args, **kwargs)
            resp = {'code': code, 'msg': msg, 'data': data}
        except Exception as e:
            resp = {'code': ResponseCode.Faild.value, 'msg': '异常错误', 'data': {}}
        finally:
            return resp
    return decorate
