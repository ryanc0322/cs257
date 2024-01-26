# WOOYEOK CHOI (2024.1.24)
# This code is for the python-psql lab in the software design course

import psycopg2
from config import config

def create_tables():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="choir",
        user="choir",
        password="spam889books"
    )

    cur = conn.cursor()

    sql_commands = [
        """
        CREATE TABLE states (
            id SERIAL PRIMARY KEY,
            state_name VARCHAR(255) NOT NULL,
            abbreviation VARCHAR(2) NOT NULL
        )
        """,
        """
        CREATE TABLE cities (
            id SERIAL PRIMARY KEY,
            city_name VARCHAR(255) NOT NULL,
            state_id INTEGER REFERENCES states(id),
            population INTEGER NOT NULL,
            latitude FLOAT NOT NULL,
            longitude FLOAT NOT NULL
        )
        """
    ]

    try:
        for sql in sql_commands:
            cur.execute(sql)

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    create_tables()

