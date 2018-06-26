import template
import pytest
import re

jobs = [
    {"queue_name": "search", "size": 100},
    {"queue_name": "common", "size": 10}
]

workers = [
    {"name": "bob", "queues":"search", "state":"busy"},
    {"name": "alice", "queues":"search", "state":"idle"}
]

rendered_ouput = template.render(jobs, workers)

@pytest.mark.parametrize('expected_content', [
    "^\# TYPE rq_enqueued_jobs gauge$",
    "^rq_enqueued_jobs{queue_name=\"search\"} 100$",
    "^rq_enqueued_jobs{queue_name=\"common\"} 10$",

    "^\# TYPE rq_workers gauge$",
    "^rq_workers{name=\"bob\", queues=\"search\", state=\"busy\"} 1$",
    "^rq_workers{name=\"alice\", queues=\"search\", state=\"idle\"} 1$",
])
def test_enqueued_jobs_stats(expected_content):
    regex = re.compile(expected_content, re.MULTILINE)
    assert regex.search(rendered_ouput) is not None
