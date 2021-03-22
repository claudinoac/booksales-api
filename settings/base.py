from tornado_sqlalchemy import SQLAlchemy
from tornado.options import options, define
from os import environ

define(
    'port',
    default=environ.get("DEFAULT_PORT", 9090),
    help='port to listen on'
)

SETTINGS = {
    'debug': environ.get("DEBUG", True),
}

DB = {
    'username': environ.get("DB_USER", "booksales"),
    'password': environ.get("DB_PWD", "booksales"),
    'host': environ.get("DB_HOST", "db"),
    'port': environ.get("DB_PORT", 5432),
    'name': environ.get("DB_NAME", "booksales")
}
DB_URL = "postgresql://{user}:{pwd}@{host}:5432/{db_name}".format(
    user=DB["username"],
    pwd=DB["password"],
    host=DB["host"],
    db_name=DB["name"]
)

DATABASE = SQLAlchemy(url=DB_URL)
