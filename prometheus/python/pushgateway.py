from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

"""
please install prometheus client through

pip install prometheus_client
"""


registry = CollectorRegistry()
g = Gauge(
    'pushgateway_job_last_success_unixtime',
    'Last time a batch job successfully finished',
    ['a', 'b'],
    registry=registry)
g.labels(a='1', b='2').set_to_current_time()
push_to_gateway('localhost:9091', job='job test', registry=registry)
