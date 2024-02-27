class Config:
    # Postgres Configs
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432

    # RabbitMQ Configs
    RABBITMQ_AUTO_ACK: bool = False
    RABBITMQ_USERNAME: str = ""
    RABBITMQ_PASSWORD: str = ""
    RABBITMQ_HOST: str = ""
    RABBITMQ_PORT: int = 5672
    RABBITMQ_QUEUE: str = ""
    RABBITMQ_VHOST: str = ""
