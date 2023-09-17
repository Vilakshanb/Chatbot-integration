import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE


def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
    )
    return connection
