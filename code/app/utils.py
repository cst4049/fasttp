import logging
import requests
from enum import Enum
from functools import wraps
from retrying import retry
from app.exceptions import HTTPError


class ResponseCode(Enum):
    """响应码"""
    Success = 0
    Faild = -1
    Unknow = -2


class Logger:

    def __init__(self, level=logging.INFO, name='root'):
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=level, format=format)
        self.logger = logging.getLogger(name)


logger = Logger().logger


def make_response(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            code, msg, data = func(*args, **kwargs)
            resp = {'code': code, 'msg': msg, 'data': data}
        except HTTPError as e:
            resp = {'code': ResponseCode.Faild.value, 'msg': 'http服务暂不可用', 'data': {}}
        except Exception as e:
            resp = {'code': ResponseCode.Faild.value, 'msg': '异常错误', 'data': {}}
        finally:
            logger.info(f'返回值: {resp}')
            return resp
    return decorate


@retry(stop_max_attempt_number=3)
def http(method, url, *args, **kwargs):
    """http请求"""
    opt = getattr(requests, method)
    resp = opt(url, *args, **kwargs)
    return resp


if __name__ == '__main__':
    logger.info('aaaa')
