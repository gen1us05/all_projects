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
query = '''CREATE TABLE users(
user_id SERIAL PRIMARY KEY,
username VARCHAR(25),
password VARCHAR(25),
firstname VARCHAR(35),
lastname VARCHAR(35),
create_date DATE DEFAULT now(),
district_id INT REFERENCES district(district_id));'''
cursor.execute(query)
connection.commit()
print('done')
