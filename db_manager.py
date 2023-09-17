import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE
import mysql.connector


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def fetch_data(query):
    connection = connect_to_db()
    if not connection:
        return None
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results


def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
    )
    return connection
