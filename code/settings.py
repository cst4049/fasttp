from typing import List
from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    blueprints: List[str] = Field(['heartbeat'], title='蓝图')


class RedisSettings(BaseSettings):
    host: str = Field('localhost', title='uri')
    port: int = Field(6379, title='uri')
    password: str = Field(None, title='密码')
    skip_full_coverage_check: bool = Field(False, title='跳过版本检查')


app_settings = AppSettings()
redis_settings = RedisSettings()
