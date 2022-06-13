import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from sqlmodel import SQLModel

from src import settings

from . import models

database_url = settings.DATABASE_URL
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_database():
    if not database_exists(database_url):
        create_database(database_url)
        print(f"Database created: {database_url}")
    return True

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         if sys.argv[1] == "createdb":
#             init_database()
#         else:
#             print("Argument valid only: createdb")
