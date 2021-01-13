from importlib import import_module
from fastapi import FastAPI

from settings import app_settings, redis_settings
from app.common import redis_client


def register_blueprints(app: FastAPI, blueprints: list[str]):
    """蓝图注册"""
    for bp in blueprints:
        mod = import_module(f'app.apis.{bp}')
        app.include_router(mod.bp)


def register_common():
    """公共组件注册"""
    redis_client.init_single(redis_settings.host, redis_settings.port, redis_settings.password)


def create_app():
    """app 实例化"""
    app = FastAPI()
    register_blueprints(app, app_settings.blueprints)
    register_common()
    return app
