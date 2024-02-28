from adapter.rabbitmq.base_rabbitmq import BaseRabbitMQ


class RabbitMQPublisher(BaseRabbitMQ):
    def __init__(self):
        super().__init__()

    def basic_publish(self, body):

        self.channel.basic_publish(
            exchange='',
            routing_key=self.rabbitmq_queue,
            body=body
        )
        print(' [*] Sent messages. To exit press CTRL+C')
