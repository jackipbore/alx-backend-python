#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='jkbore',
            password='Technology@1',
            database='ALX_prodev'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None

def stream_users_in_batches(batch_size):
    """
    Generator to fetch users from the user_data table in batches of size batch_size.
    """
    connection = connect_to_prodev()
    if not connection:
        return

    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
    Process batches fetched from stream_users_in_batches, yielding users older than 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user
