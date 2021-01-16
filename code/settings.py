from typing import List
from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    host: str = Field('127.0.0.1', title='主机')
    port: int = Field(9000, title='端口')
    blueprints: List[str] = Field(['heartbeat'], title='蓝图')


class RedisSingleSettings(BaseSettings):
    """单机版redis"""
    host: str = Field('localhost', title='主机')
    port: int = Field(6379, title='端口')
    password: str = Field(None, title='密码')
    skip_full_coverage_check: bool = Field(False, title='跳过版本检查')


class MysqlSettings(BaseSettings):
    uri: str = Field('mysql+mysqlconnector://root:123456@localhost:3306/fastapi')


class MongoSettings(BaseSettings):
    uri: str = Field('mongodb://localhost:27017/test')


app_settings = AppSettings()
redis_settings = RedisSingleSettings()
mysql_settings = MysqlSettings()
mongo_settings = MongoSettings()
