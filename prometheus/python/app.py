import prometheus_client as prom
import random
import time


if __name__ == '__main__':

   counter = prom.Counter('python_my_counter', 'This is my counter', ['method', 'endpoint'])
   gauge = prom.Gauge('python_my_gauge', 'This is my gauge', ['hostname', 'interface'])

   prom.start_http_server(8000)
   while True:
       counter.labels(method='get', endpoint='/').inc(random.random())
       counter.labels(method='post', endpoint='/submit').inc(random.random())
       gauge.labels(hostname='a.b.c', interface='eth0').set(random.random() * 15 - 5)
       time.sleep(1)
