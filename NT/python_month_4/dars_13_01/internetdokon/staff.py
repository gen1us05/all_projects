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
query = '''CREATE TABLE payment(
payment_id SERIAL PRIMARY KEY,
amount INT,
pay_date DATE DEFAULT now(),
user_id INT REFERENCES users(user_id),
product_id INT REFERENCES product(product_id),
staff_id INT REFERENCES staff(staff_id));'''
cursor.execute(query)
connection.commit()
print('done')
