from typing import Union, Any

import redis
from redis.cluster import ClusterNode, RedisCluster
from redis.sentinel import Sentinel
from redis.cluster import ClusterNode
from redis.connection import Connection, SSLConnection
from auth_app import AuthApp
from configs import auth_config


class RedisClientWrapper:

    def __init__(self):
        self._client = None

    def initialize(self, client):
        if self._client is None:
            self._client = client

    def __getattr__(self, item):
        if self.client is None:
            raise RuntimeError("Redis client is not initialized. Call init_app first.")
        return getattr(self._client, item)


redis_client = RedisClientWrapper()

def init_app(app: AuthApp):
    global redis_client
    connection_class: type[Union[Connection, SSLConnection]] = Connection
    if auth_config.REDIS_USE_SSL:
        connection_class = SSLConnection

    redis_params: dict[str, Any] = {
        "username": auth_config.REDIS_USERNAME,
        "password": auth_config.REDIS_PASSWORD or None,
        "db": auth_config.REDIS_DB,
        "encoding": "utf-8",
        "encoding_errors": "strict",
        "decode_responses": False,
    }

    # 哨兵模式
    if auth_config.REDIS_USE_SENTINEL:
        master = get_client_of_sentinel(redis_params)
        redis_client.initialize(master)
    # 集群模式
    elif auth_config.REDIS_USE_CLUSTERS:
        cluster = get_client_of_cluster()
        redis_client.initialize(cluster)
    # 单机模式
    else:
        single = get_client_of_single(connection_class, redis_params)
        redis_client.initialize(single)

    app.extensions["redis"] = redis_client


def get_client_of_single(connection_class, redis_params):
    redis_params.update(
        {
            "host": auth_config.REDIS_HOST,
            "port": auth_config.REDIS_PORT,
            "connection_class": connection_class,
        }
    )
    pool = redis.ConnectionPool(**redis_params)
    single = redis.Redis(connection_pool=pool)
    return single


def get_client_of_cluster():
    assert auth_config.REDIS_CLUSTERS is not None, "REDIS_CLUSTERS must be set when REDIS_USE_CLUSTERS is True"
    nodes = [
        ClusterNode(host=node.split(":")[0], port=int(node.split(":")[1])) for node in
        auth_config.REDIS_CLUSTERS.split(',')
    ]
    cluster = RedisCluster(startup_nodes=nodes, password=auth_config.REDIS_CLUSTERS_PASSWORD)
    return cluster


def get_client_of_sentinel(redis_params):
    assert auth_config.REDIS_SENTINELS is not None, "REDIS_SENTINELS must be set when REDIS_USE_SENTINEL is True"
    sentinel_hosts = [
        (node.split(":")[0], int(node.split(":")[1])) for node in auth_config.REDIS_SENTINELS.split(",")
    ]
    sentinel = Sentinel(
        sentinel_hosts,
        sentinel_kwargs={
            "socket_timeout": auth_config.REDIS_SENTINEL_SOCKET_TIMEOUT,
            "username": auth_config.REDIS_SENTINEL_USERNAME,
            "password": auth_config.REDIS_SENTINEL_PASSWORD,
        },
    )
    master = sentinel.master_for(auth_config.REDIS_SENTINEL_SERVICE_NAME, **redis_params)
    return master
