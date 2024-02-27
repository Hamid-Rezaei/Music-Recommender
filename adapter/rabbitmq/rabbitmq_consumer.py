import json

import pika
from pika import BlockingConnection


class AbstractBaseRabbitMQConsumer:
    REPORTED_CLASS = "RabbitMQ"

    def __init__(self):
        self.rabbitmq_user_name: str
        self.rabbitmq_password: str
        self.rabbitmq_host: str
        self.rabbitmq_vhost: str
        self.rabbitmq_port: int
        self.rabbitmq_queue: str
        self.channel: BlockingConnection.channel

    def purge_queue(self):
        channel = self._initialize_connection()
        channel.queue_purge(queue=self.rabbitmq_queue)

    def _initialize_connection(self):
        credentials = pika.PlainCredentials(self.rabbitmq_user_name, self.rabbitmq_password)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.rabbitmq_host, port=self.rabbitmq_port, credentials=credentials,
                                      virtual_host=self.rabbitmq_vhost))
        channel = connection.channel()
        return channel

    def callback(self, ch, method, properties, body: bytes):
        message_dict: dict = json.loads(body.decode(encoding="UTF-8"))
        if message_dict.get("EventType"):
            print(" [x] Received instrument trade event:  %r" % message_dict)

    def basic_consume(self, callback):
        auto_ack = Configuration.config().RABBITMQ_AUTO_ACK

        self.channel.basic_consume(queue=self.rabbitmq_queue,
                                   auto_ack=auto_ack,
                                   on_message_callback=callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


class BaseRabbitMQConsumer(AbstractBaseRabbitMQConsumer):
    def __init__(self):
        super().__init__()
        self.rabbitmq_user_name = SCLConfig.RABBITMQ_USERNAME
        self.rabbitmq_password = SCLConfig.RABBITMQ_PASSWORD
        self.rabbitmq_host = SCLConfig.RABBITMQ_HOST
        self.rabbitmq_vhost = SCLConfig.RABBITMQ_VHOST
        self.rabbitmq_port = SCLConfig.RABBITMQ_PORT
        self.rabbitmq_queue = SCLConfig.RABBITMQ_QUEUE
