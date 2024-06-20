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
query = '''CREATE TABLE region(
region_id SERIAL PRIMARY KEY,
name VARCHAR(35),
city_id INT REFERENCES city(city_id));'''
cursor.execute(query)
connection.commit()
print('done')
