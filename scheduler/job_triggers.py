from apscheduler.triggers.cron import CronTrigger
from pytz import timezone


class JobTriggers:
    def __init__(self):
        pass

    @staticmethod
    def get_every_5_minutes_trigger():
        return CronTrigger(
            # day_of_week="sat,sun,mon,tue,wed",
            # hour="8-20",
            # minute="*/5",
            # timezone=timezone("Asia/Tehran")
            second=30
        )
