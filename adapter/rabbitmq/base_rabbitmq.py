import pika
from pika import BlockingConnection

from project.configuration.config import Config


class AbstractBaseRabbitMQ:
    REPORTED_CLASS = "RabbitMQ"

    def __init__(self):
        self.rabbitmq_user_name: str
        self.rabbitmq_password: str
        self.rabbitmq_host: str
        self.rabbitmq_vhost: str
        self.rabbitmq_port: int
        self.rabbitmq_queue: str
        self.channel: BlockingConnection.channel

    def _initialize_connection(self):
        credentials = pika.PlainCredentials(self.rabbitmq_user_name, self.rabbitmq_password)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.rabbitmq_host,
                port=self.rabbitmq_port,
                credentials=credentials,
                virtual_host=self.rabbitmq_vhost
            )
        )
        channel = connection.channel()
        return channel

    def purge_queue(self):
        self.channel.queue_purge(queue=self.rabbitmq_queue)

    def declare_queue(self):
        self.channel.queue_declare(queue=self.rabbitmq_queue)


class BaseRabbitMQ(AbstractBaseRabbitMQ):
    def __init__(self):
        super().__init__()
        self.rabbitmq_user_name = Config.RABBITMQ_USERNAME
        self.rabbitmq_password = Config.RABBITMQ_PASSWORD
        self.rabbitmq_host = Config.RABBITMQ_HOST
        self.rabbitmq_vhost = Config.RABBITMQ_VHOST
        self.rabbitmq_port = Config.RABBITMQ_PORT
        self.rabbitmq_queue = Config.RABBITMQ_QUEUE
        self.channel = self._initialize_connection()
        self.declare_queue()
