import psycopg2 as psql
import os


class Database:
    @staticmethod
    def connect(query):

        postgres_db = psql.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            database=os.getenv('DATABASE'),
            password=os.getenv('PASSWORD')
        )
        cursor = postgres_db.cursor()
        cursor.execute(query)
        postgres_db.commit()
        return "Done"