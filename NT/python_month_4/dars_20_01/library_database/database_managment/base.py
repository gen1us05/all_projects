import psycopg2 as psql
import os

class Database:
    @staticmethod
    def connect(query):

        postgres_db = psql.connect(
            host='localhost',
            user='postgres',
            database='library',
            password='password'
        )

        cursor = postgres_db.cursor()
        cursor.execute(query)
        postgres_db.commit()
        return "Done"