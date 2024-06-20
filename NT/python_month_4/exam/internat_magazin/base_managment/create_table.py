from base import Database


def create_table():
    type = f"""
        CREATE TABLE type(
            type_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            color VARCHAR(25),
            expiration_date VARCHAR(20),
            size VARCHAR(35))"""

    product = f"""
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            price smallint,
            type_id INT REFERENCES type(type_id),
            count smallint)"""

    payment = f"""
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            payment_type VARCHAR(25))"""

    users = f"""
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(35),
            last_name VARCHAR(35),
            email VARCHAR(20))"""

    sell_product = f"""
        CREATE TABLE sell_product(
            sell_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(user_id),
            product_id INT REFERENCES product(product_id),
            payment_id INT REFERENCES payment(payment_id),
            sold_time TIMESTAMP DEFAULT now())"""

    sold_products = f"""
        CREATE TABLE sold_products(
            sold_products_id SERIAL PRIMARY KEY,
            count integer,
            price int,
            user_id INT REFERENCES users(user_id),
            product_id INT REFERENCES product(product_id))"""

    admin = f"""
        CREATE TABLE admin(
            first_name VARCHAR(35),
            last_name VARCHAR(35),
            email VARCHAR(20),
            product_id INT REFERENCES product(product_id))"""


    tables = {
        "type": type,
        "product": product,
        "payment": payment,
        "user": users,
        "sell_product": sell_product,
        "sold_products": sold_products,
        "admin": admin}

    for table, query in tables.items():
        print(table + Database.connect(query))

if __name__ == "__main__":
    create_table()
