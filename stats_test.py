import stats
from rq import Worker, Queue

queue = Queue("echo", connection=stats.CONN)
worker = Worker(["searches", "test"], name="test_worker", connection=stats.CONN)

def teardown_function():
    queue.delete(delete_jobs=True)
    worker.register_death()

def test_stat_scrape_default():
    queue.enqueue("echo_worker", "HEY!")
    queue.enqueue("echo_worker", "HO!")
    worker.register_birth()

    jobs, workers = stats.scrape()
    assert jobs == [{"queue_name": "echo", "size": 2}]
    assert workers == [{"name": "test_worker", "queues": "searches,test", "state": "?"}]

def test_stat_scrape_disabled_workers_scraping():
    queue.enqueue("echo_worker", "HEY!")
    queue.enqueue("echo_worker", "HO!")
    worker.register_birth()
    stats.SCRAPE_WORKERS = False
    jobs, workers = stats.scrape()
    assert jobs == [{"queue_name": "echo", "size": 2}]
    assert workers == []

def test_stat_scrape_enabled_workers_scraping():
    queue.enqueue("echo_worker", "HEY!")
    queue.enqueue("echo_worker", "HO!")
    worker.register_birth()
    stats.SCRAPE_WORKERS = True
    jobs, workers = stats.scrape()
    assert jobs == [{"queue_name": "echo", "size": 2}]
    assert workers == [{"name": "test_worker", "queues": "searches,test", "state": "?"}]
