import psycopg2 as psql
'''
    connect psql
'''


connection = psql.connect(
    host="localhost",
    database="internet_dokon",
    user="postgres",
    password="password"
)
'''cursor'''

cursor = connection.cursor()
query = '''CREATE TABLE city(
city_id SERIAL PRIMARY KEY,
name VARCHAR(35),
country_id INT REFERENCES country(country_id));'''
cursor.execute(query)
connection.commit()
print('done')
