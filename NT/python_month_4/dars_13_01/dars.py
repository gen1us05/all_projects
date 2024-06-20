import psycopg2 as psql

postgres_db = psql.connect(
    host ="localhost",
    database = "e_commerse",
    user="postgres",
    password="password"
)

cursor = postgres_db.cursor()
query = "CREATE TABLE country(country_id SERIAL PRIMARY KEY, name VARCHAR(20))"
cursor.execute(query)

cursor.execute("INSERT INTO country(name) VALUES ('Uzbekistan')")
cursor.execute("INSERT INTO country(name) VALUES ('Korea')")
cursor.execute("INSERT INTO country(name) VALUES ('California')")


cursor.execute("SELECT * FROM country")


print()