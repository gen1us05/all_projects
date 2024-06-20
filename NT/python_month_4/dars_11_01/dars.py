import psycopg2 as psql


postgres_db = psql.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="password"
)


