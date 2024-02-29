from adapter.rabbitmq.rabbitmq_consumer import RabbitMQConsumer
from main.logic.search_music_shazam_logic import SearchMusicShazamLogic


class SearchEventConsumer:
    def __init__(self):
        super().__init__()
        self.search_music_rabbit_consumer_adapter = RabbitMQConsumer()
        self.search_music_shazam_logic = SearchMusicShazamLogic()

    def callback(self, ch, method, properties, body: bytes):
        print(" [x] Received " + str(body))
        self.search_music_shazam_logic.find_music_by_shazam(audio=None)

    def consume(self):
        self.search_music_rabbit_consumer_adapter.basic_consume_(
            callback=self.callback
        )
