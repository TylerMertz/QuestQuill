from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import sys

from app.core.config import settings as settings

connection_str = f"postgresql+psycopg2://{settings.pg_username}:{settings.pg_password}@{settings.pg_host}:{settings.pg_port}/{settings.pg_db}"
print(connection_str)

engine = create_engine(connection_str)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def db_connection():
    db = Session()
    try:
        yield db
    finally:
        db.close()