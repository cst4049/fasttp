from typing import List
from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    blueprints: List[str] = Field(['heartbeat'], title='蓝图')


class RedisSettings(BaseSettings):
    host: str = Field('localhost', title='主机')
    port: int = Field(6379, title='端口')
    password: str = Field(None, title='密码')
    skip_full_coverage_check: bool = Field(False, title='跳过版本检查')


class MysqlSettings(BaseSettings):
    uri: str = Field('mysql+mysqlconnector://root:123456@localhost:3306/fastapi')
    host: str = Field('localhost', title='主机')
    port: int = Field(3306, title='端口')
    user: str = Field('root', title='帐号')
    password: str = Field('123456', title='密码')
    database: str = Field('fastapi', title='数据库')


app_settings = AppSettings()
redis_settings = RedisSettings()
mysql_settings = MysqlSettings()
