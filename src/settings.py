import os
from dotenv import load_dotenv

load_dotenv()


def get_connection_string():
    engine = os.environ.get("DB_ENGINE")
    dbhost = os.environ.get("DB_HOST")
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    dbname = os.environ.get("DB_NAME")
    return f"{engine}://{username}:{password}@{dbhost}/{dbname}"


# Database Setting
SQLALCHEMY_DATABASE_URL = get_connection_string()

INFO_GENERATE_TOKEN = {
    "SECRET_KEY": os.environ.get("SECRET_KEY"),
    "ALGORITHM": os.environ.get("ALGORITHM", default="HS256"),
    "ACCESS_TOKEN_EXPIRE_MINUTES": int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", default="30"))
}

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", default="1qaZ@wsx")
