from redis import Redis
from rediscluster import RedisCluster


class RedisClient:

    def __init__(self):
        self.client = None

    def init_single(self, host, port, password):
        self.client = Redis(host, port, password)

    def init_cluster(self, startup_nodes, password, skip_full_coverage_check):
        self.client = RedisCluster(startup_nodes, password,
                                   skip_full_coverage_check=skip_full_coverage_check)


redis_client = RedisClient()
