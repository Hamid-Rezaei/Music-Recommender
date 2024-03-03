from django.core.management.base import BaseCommand

from project.configuration.config import Config
from project.configuration.configuration import Configuration
from scheduler.scheduler import Scheduler


class Command(BaseCommand):
    help = 'start scheduler service'

    def __init__(self):
        super().__init__()

    def handle(self, *args, **kwargs):
        Configuration.configure(Config)
        Scheduler().start()
