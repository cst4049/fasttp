from fastapi import APIRouter
from app.utils import make_response, ResponseCode


route = APIRouter()


@make_response
def heartbeat():
    """心跳检测接口"""
    return ResponseCode.Success.value, '', {}


route.add_api_route(path='/heartbeat', name='heartbeat', endpoint=heartbeat, tags=['心跳检测'])
