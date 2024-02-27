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


class DatabaseBaseConfig2:
    DATABASE2_URI: str = None
    SQLALCHEMY2_TRACK_MODIFICATIONS: bool = False  # for performance overhead

    SQLALCHEMY2_ENGINE_OPTIONS: dict = {'isolation_level': 'REPEATABLE READ', "pool_pre_ping": True,
                                        "pool_recycle": 3600, "pool_size": 100}
    DJANGO2_DB_ENGINE = None
    RDB2_NAME = None
    RDB2_USERNAME = None
    RDB2_PASSWORD = None
    RDB2_HOST = None
    RDB2_PORT = None


class DatabaseBaseConfig3:
    DATABASE3_URI: str = None
    SQLALCHEMY3_TRACK_MODIFICATIONS: bool = False  # for performance overhead

    SQLALCHEMY3_ENGINE_OPTIONS: dict = {'isolation_level': 'REPEATABLE READ', "pool_pre_ping": True,
                                        "pool_recycle": 3600, "pool_size": 100}
    DJANGO_DB3_ENGINE = None
    RDB3_NAME = None
    RDB3_USERNAME = None
    RDB3_PASSWORD = None
    RDB3_HOST = None
    RDB3_PORT = None


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


class APIConfig:
    API_URL_PREFIX: str = "/api/"
    API_URL_VERSION: str = "v1/"


class UtilsConfig:
    UTILS_PRICE_NOTICE_DB_READ_LIVENESS_IN_SECONDS = 5 * 60  # 5 Minutes


class CommonsBaseConfig(
    WebFrameworkConfig,
    DatabaseBaseConfig,
    EnvironmentConfig,
    PaginationBaseConfig,
    RedisBaseConfig,
    APIConfig,
    JWTConfig,
    UtilsConfig
):
    pass
