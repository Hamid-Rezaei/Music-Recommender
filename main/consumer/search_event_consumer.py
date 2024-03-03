import json

from django.db import transaction

from adapter.rabbitmq.rabbitmq_consumer import RabbitMQConsumer
from main.logic.search_music_shazam_logic import SearchMusicShazamLogic


class SearchEventConsumerService:
    def __init__(self):
        super().__init__()
        self.search_music_rabbit_consumer_adapter = RabbitMQConsumer()
        self.search_music_shazam_logic = SearchMusicShazamLogic()

    def callback(self, ch, method, properties, body: bytes):
        body = json.loads(body)
        print(" [x] Received %r" % body)
        self.serve_event(event=body)

    def consume(self):
        self.search_music_rabbit_consumer_adapter.basic_consume_(callback=self.callback)

    def start(self):
        self.consume()

    def serve_event(self, event):
        print('SERVICE', event)

        with transaction.atomic():
            self.search_music_shazam_logic.recognize_music_by_shazam(audio_uri=event['audio_uri'])

            # TODO: spotify

            # TODO: database
