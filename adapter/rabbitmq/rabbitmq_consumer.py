import json

from adapter.rabbitmq.base_rabbitmq import BaseRabbitMQ
from project.configuration.configuration import Configuration


class RabbitMQConsumer(BaseRabbitMQ):

    def __init__(self):
        super().__init__()

    def callback(self, ch, method, properties, body: bytes):
        message_dict: dict = json.loads(body.decode(encoding="UTF-8"))
        if message_dict.get("EventType"):
            print(" [x] Received search music event:  %r" % message_dict)

    def basic_consume(self, callback):
        auto_ack = Configuration.config().RABBITMQ_AUTO_ACK

        self.channel.basic_consume(
            queue=self.rabbitmq_queue,
            auto_ack=auto_ack,
            on_message_callback=callback
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
