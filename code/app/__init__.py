from importlib import import_module
from fastapi import FastAPI
from app.apis import heartbeat

from settings import BluePrints


def register_blueprints(app: FastAPI, blueprints: list[str]):
    """蓝图注册"""
    for bp in blueprints:
        mod = import_module(f'app.apis.{bp}')
        app.include_router(mod.route)


def create_app():
    app = FastAPI()
    register_blueprints(app, BluePrints)
    return app
