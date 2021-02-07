import os

import psycopg2
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

SQL_USER = os.environ.get("SQL_USER")
SQL_PASS = os.environ.get("SQL_PASS")
SQL_HOST = os.environ.get("SQL_HOST")
SQL_PORT = os.environ.get("SQL_PORT")
SQL_DB = os.environ.get("SQL_DB")
