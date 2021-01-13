import requests


def test_heartbeat():
    """心跳检测接口"""
    resp = requests.get('http://localhost:9000/heartbeat')
    assert resp.status_code == 200
