import os

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore

from project.configuration.config import Config
from scheduler.job_triggers import JobTriggers

from scheduler.jobs import Jobs


class Scheduler:
    def __init__(self):
        self.jobs = Jobs()
        self.scheduler: BlockingScheduler = self._initiate_scheduler()

    def _initiate_scheduler(self) -> BlockingScheduler:
        try:

            job_stores = {
                'redis': RedisJobStore(db=Config.REDIS_DB, host=Config.REDIS_HOST, port=Config.REDIS_PORT),
            }
            executors = {
                'default': ThreadPoolExecutor(20),
                'processpool': ProcessPoolExecutor(5)
            }
            job_defaults = {
                'coalesce': False,
                'max_instances': 3
            }
            return BlockingScheduler(jobstores=job_stores, executors=executors, job_defaults=job_defaults)
        except Exception:
            raise

    def start(self):
        try:

            self.scheduler.add_job(
                self.jobs.update_search_request_status,
                JobTriggers.get_every_5_minutes_trigger()
            )

            print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
            self.scheduler.print_jobs()

            try:
                self.scheduler.start()
            except (KeyboardInterrupt, SystemExit):
                pass
        except Exception:
            raise
