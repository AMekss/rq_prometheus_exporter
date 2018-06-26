import os, redis
from rq import Worker, Queue, Connection

CONN = redis.from_url(os.getenv('RQ_REDIS_URI'))

def scrape():
    enqueued_jobs = []
    workers = []

    enqueued_jobs = [
        dict(queue_name=q.name, size=q.count)
        for q in Queue.all(connection=CONN)
    ]

    workers = [
        dict(name=w.name, queues=_serialize_queue_names(w), state=str(w.get_state()))
        for w in Worker.all(connection=CONN)
    ]

    return enqueued_jobs, workers

def _serialize_queue_names(worker):
    return ",".join([q.name for q in worker.queues])
