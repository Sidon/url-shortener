from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "Bemobi url-shortenerr"
VERSION = "0.1.1"
SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")
DATABASE_URL = config("DATABASE_URL", cast=str, default="sqlite:///shortener.db")
BASE_URL = "http://localhost:8004"
