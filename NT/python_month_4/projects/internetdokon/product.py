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
query = '''CREATE TABLE product(
product_id SERIAL PRIMARY KEY,
name VARCHAR(35),
count INT DEFAULT 0,
price INT,
start_date DATE,
end_date DATE,
category_id INT REFERENCES category(category_id));'''
cursor.execute(query)
connection.commit()
print('done')
