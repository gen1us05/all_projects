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
query = '''CREATE TABLE district(
district_id SERIAL PRIMARY KEY,
name VARCHAR(35) NOT NULL,
region_id INT REFERENCES region(region_id));'''
cursor.execute(query)
connection.commit()
print('done')
