ENQUEUED_JOBS_STATS_TEMPLATE = "rq_enqueued_jobs{{queue_name=\"{queue_name}\"}} {size}\n"
WORKERS_STATS_TEMPLATE = "rq_workers{{name=\"{name}\", queues=\"{queues}\", state=\"{state}\"}} 1\n"
TEMPLATE = \
"""# HELP rq_enqueued_jobs The total number of enqueued jobs.
# TYPE rq_enqueued_jobs gauge
{enqueued_jobs_stats}

# HELP rq_workers The number of workers performing jobs.
# TYPE rq_workers gauge
{workers_stats}"""


def render(jobs, workers):
    values = {
        "enqueued_jobs_stats": _jobs_stats(jobs),
        "workers_stats": _workers_stats(workers)
    }

    return TEMPLATE.format(**values)


def _jobs_stats(jobs):
    values = []
    for job in jobs:
        values.append(ENQUEUED_JOBS_STATS_TEMPLATE.format(**job))

    return "".join(values)


def _workers_stats(workers):
    values = []
    for worker in workers:
        values.append(WORKERS_STATS_TEMPLATE.format(**worker))

    return "".join(values)
