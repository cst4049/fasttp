from app.common import redis_client
from settings import redis_settings


def test_redis_single():
    """单机redis"""
    redis_client.init_single(redis_settings.host, redis_settings.port, redis_settings.password)
    redis_client.client.set('a', 1, ex=10)
    val = redis_client.client.get('a')
    assert val == b'1'
