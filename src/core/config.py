import os
import secrets
import databases
import sqlalchemy
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, RedisDsn, root_validator
from databases import DatabaseURL


class Config(BaseSettings):
    PROJECT_NAME: str = 'fastapi_mongo'
    VERSION: str = '1.0.0'


settings = Config()
# database = databases.Database(settings.DATABASE_URL)
# metadata = sqlalchemy.MetaData()
