from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from pydantic import Extra


class Settings(BaseSettings):
    # OPEN_API_KEY:str
    PG_HOST: str
    PG_USER: str
    PG_PASSWD: str
    PG_PORT: str
    PG_DB: str
    CELERY_BROKER_URL:str = "amqp://neuron_rbt_user:neuron@rabbitmq:5672//"
    PG_URI: PostgresDsn

    class Config:
        env_file = None
        env_file_encoding = "utf-8"
        extra = Extra.allow
        env_prefix = "NE_"


settings = Settings()
