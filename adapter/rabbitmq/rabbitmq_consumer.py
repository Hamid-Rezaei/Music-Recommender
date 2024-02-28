import json

from adapter.rabbitmq.base_rabbitmq import BaseRabbitMQ
from project.configuration.configuration import Configuration


class RabbitMQConsumer(BaseRabbitMQ):

    def __init__(self):
        super().__init__()

    def callback(self, ch, method, properties, body: bytes):
        print(" [x] Received " + str(body))

    def basic_consume_(self, callback):
        auto_ack = Configuration.config().RABBITMQ_AUTO_ACK

        self.channel.basic_consume(
            queue=self.rabbitmq_queue,
            auto_ack=auto_ack,
            on_message_callback=callback
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
