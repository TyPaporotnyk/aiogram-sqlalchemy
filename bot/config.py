from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    bot_token: SecretStr
    db_url: str
    redis_url: str

    postgres_db: str
    postgres_user: str
    postgres_password: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
