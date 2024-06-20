from base import Database
import datetime


def create_table():
    product = f"""
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            brought_time  TIMESTAMP DEFAULT now(),
            expiration_date VARCHAR(50),
            price smallint,
            count int)"""

    payment = f"""
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            price smallint,
            payment_type VARCHAR(25))"""

    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            gorod_name VARCHAR(30),
            street_name VARCHAR(30),
            home_number VARCHAR(25))"""

    buyer = f"""
        CREATE TABLE buyer(
            buyer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            address_id INT REFERENCES address(address_id))"""

    staff = f"""
        CREATE TABLE staff(
            staff_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            birth_year DATE,
            address_id INT REFERENCES address(address_id))"""

    coll_center = f"""
        CREATE TABLE coll_center(
            c_center_id SERIAL PRIMARY KEY,
            staff_id INT REFERENCES staff(staff_id),
            phone_number numeric(12),
            working_time VARCHAR(30)"""

    filial = f"""
        CREATE TABLE filial(
            filial_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(100),
            google_location VARCHAR(55),
            address_id INT REFERENCES address(address_id),
            c_center_id INT REFERENCES coll_center(coll_center_id)"""

    sell_product = f"""
        CREATE TABLE sell_product(
            sell_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            payment_id INT REFERENCES payment(payment_id),
            staff_id INT REFERENCES staff(staff_id),
            buyer_id INT REFERENCES buyer(buyer_id),
            filial_id INT REFERENCES filial(filial_id)"""

    sold_id = f"""
        CREATE TABLE sold_id(
            sell_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            payment_id INT REFERENCES payment(payment_id),
            sell_id INT REFERENCES sell(sell_id),
            buyer_id INT REFERENCES buyer(buyer_id),
            filial_id INT REFERENCES filial(filial_id)"""

    tables = {
        'product': product,
        'payment': payment,
        'address': address,
        'buyer': buyer,
        'staff': staff,
        'coll_center': coll_center,
        'filial': filial,
        'sell_product': sell_product,
        'sold_id': sold_id
    }

    for table, query in tables.items():
        print(table + Database.connect(query))


if __name__ == '__main__':
    create_table()