import stats
from rq import Worker, Queue, Connection

queue = Queue("echo", connection=stats.CONN)
worker = Worker(["searches", "test"], name="test_worker", connection=stats.CONN)

def teardown_function():
    queue.delete(delete_jobs=True)
    worker.register_death()

def test_stat_scrape():
    queue.enqueue("echo_worker", "HEY!")
    queue.enqueue("echo_worker", "HO!")
    worker.register_birth()

    jobs, workers = stats.scrape()
    assert jobs == [{"queue_name": "echo", "size": 2}]
    assert workers == [{"name": "test_worker", "queues": "searches,test", "state": "?"}]
