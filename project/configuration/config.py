class Config:
    # General
    FILES_FOLDER: str = ""

    # Postgres Configs
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432

    # Redis Config
    REDIS_HOST: str = None
    REDIS_SLAVE_HOST: str = None
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = None
    REDIS_USERNAME: str = None
    REDIS_DECODE_RESPONSES: bool = True

    # RabbitMQ Configs
    RABBITMQ_AUTO_ACK: bool = False
    RABBITMQ_USERNAME: str = ""
    RABBITMQ_PASSWORD: str = ""
    RABBITMQ_HOST: str = ""
    RABBITMQ_PORT: int = 5672
    RABBITMQ_QUEUE: str = ""
    RABBITMQ_VHOST: str = ""

    # S3 Configs
    ENDPOINT_URL: str = ""
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_STORAGE_BUCKET_NAME: str = ""

    # ShazamAPI Configs
    SHAZAM_API_KEY: str = ""
    SHAZAM_URL: str = ""
    SHAZAM_HOST: str = ""

    # MailGun Configs
    MAIL_URL: str = ""
    MAIL_API_KEY: str = ""
    MAIL_DOMAIN_NAME: str = ""
