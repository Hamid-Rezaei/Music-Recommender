class ConfigConstants:
    RUN_ENV_TYPE_DEVELOPMENT = "development"
    RUN_ENV_TYPE_STAGE = "stage"
    RUN_ENV_TYPE_PRODUCTION = "production"


class EnvironmentConfig:
    RUN_ENV_TYPE: str = ConfigConstants.RUN_ENV_TYPE_DEVELOPMENT

    @classmethod
    def is_development_env(cls):
        return cls.is_debug()

    @classmethod
    def is_debug(cls):
        return (cls.RUN_ENV_TYPE == ConfigConstants.RUN_ENV_TYPE_DEVELOPMENT)


class WebFrameworkConfig:
    APP_SECRET_KEY: str = None
    APP_NAME: str = None
    WEB_RUN_PORT: int = 8000
    HEALTH_RUN_PORT: int = 8010


class JWTConfig:
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
    JWT_ALGORITHM = "HS256"
    JWT_AUTHORIZATION_HEADER_NAME = "authorization"
    JWT_AUTHORIZATION_HEADER_PREFIX = "Bearer"
    JWT_CLAIM_USER_ID = "user_id"
    JWT_CLAIM_USERNAME = "username"
    JWT_CLAIM_FULLNAME = "fullname"
    JWT_CLAIM_ROLES = "roles"


class RedisBaseConfig:
    REDIS_HOST: str = None
    REDIS_SLAVE_HOST: str = None
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = None
    REDIS_USERNAME: str = None
    REDIS_DECODE_RESPONSES: bool = True

    REDIS2_HOST: str = None
    REDIS2_PORT: int = 6379
    REDIS2_DB: int = 0
    REDIS2_PASSWORD: str = None
    REDIS2_USERNAME: str = None
    REDIS2_DECODE_RESPONSES: bool = True

    REDIS3_HOST: str = None
    REDIS3_PORT: int = 6379
    REDIS3_DB: int = 0
    REDIS3_PASSWORD: str = None
    REDIS3_USERNAME: str = None
    REDIS3_DECODE_RESPONSES: bool = True


class DatabaseBaseConfig:
    DATABASE_URI: str = None
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False  # for performance overhead

    SQLALCHEMY_ENGINE_OPTIONS: dict = {'isolation_level': 'REPEATABLE READ', "pool_pre_ping": True,
                                       "pool_recycle": 3600, "pool_size": 100}
    DJANGO_DB_ENGINE = None
    RDB_NAME = None
    RDB_USERNAME = None
    RDB_PASSWORD = None
    RDB_HOST = None
    RDB_PORT = None


class PostgresDatabaseConfig(DatabaseBaseConfig):
    DJANGO_DB_ENGINE = "django.db.backends.postgresql_psycopg2"
    RDB_NAME = None
    RDB_USERNAME = None
    RDB_PASSWORD = None
    RDB_HOST = None
    RDB_PORT = 5432


class PaginationBaseConfig:
    DEFAULT_PAGE_NUMBER: int = 1
    DEFAULT_PAGE_SIZE: int = 25


class S3Config:
    ENDPOINT_URL = None
    AWS_ACCESS_KEY_ID = None
    AWS_SECRET_ACCESS_KEY = None
    AWS_STORAGE_BUCKET_NAME = None


class CommonsBaseConfig(
    PostgresDatabaseConfig,
    WebFrameworkConfig,
    DatabaseBaseConfig,
    EnvironmentConfig,
    PaginationBaseConfig,
    RedisBaseConfig,
    JWTConfig,
    S3Config
):
    pass
