from django.core.management.base import BaseCommand

from main.consumer.search_event_consumer import SearchEventConsumer
from project.configuration.config import Config
from project.configuration.configuration import Configuration


class Command(BaseCommand):
    help = 'start rabbitmq consumer'

    def __init__(self):
        super().__init__()

    def handle(self, *args, **kwargs):
        Configuration.configure(Config)
        SearchEventConsumer().consume()
