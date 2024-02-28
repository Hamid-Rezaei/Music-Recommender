from adapter.rabbitmq.rabbitmq_consumer import RabbitMQConsumer


class SearchEventConsumer:
    def __init__(self):
        super().__init__()
        self.search_music_rabbit_consumer_adapter = RabbitMQConsumer()

    def consume(self):
        self.search_music_rabbit_consumer_adapter.basic_consume_(
            callback=self.search_music_rabbit_consumer_adapter.callback
        )
