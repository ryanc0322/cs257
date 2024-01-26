import psycopg2

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
            state_name VARCHAR(255),
            abbreviation VARCHAR(2)
        )
        """,
        """
        CREATE TABLE cities (
            city_name VARCHAR(255),
            state_name VARCHAR(255),
            population INTEGER,
            latitude FLOAT,
            longitude FLOAT
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

