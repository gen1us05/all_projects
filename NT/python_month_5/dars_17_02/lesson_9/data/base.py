import psycopg2 as db
import os

from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "delete", "update", "create", "drop"]
        if query_type in data:
            database.commit()

            if query_type == "insert":
                return "Inserted"

            elif query_type == "delete":
                return "Deleted"

            elif query_type == "update":
                return "Updated"

            elif query_type == "create":
                return "created"
            elif query_type == "drop":
                return "Droped"

        else:
            return cursor.fetchall()