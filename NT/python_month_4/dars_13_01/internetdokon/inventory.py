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
query = '''CREATE TABLE inventory(
inventory_id SERIAL PRIMARY KEY,
district_id INT REFERENCES district(district_id),
product_id INT REFERENCES product(product_id));'''
cursor.execute(query)
connection.commit()
print('done')
