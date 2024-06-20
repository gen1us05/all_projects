from base import Database


def create_table():
    book = f"""
        CREATE TABLE book(
            book_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description TEXT,
            count INT,
            language VARCHAR(15),
            created_at TIMESTAMP DEFAULT now())"""

    author = f"""
        CREATE TABLE author(
            author_id SERIAL PRIMARY KEY,
            first_name VARCHAR(25),
            last_name VARCHAR(25),
            birth_year DATE,
            last_update TIMESTAMP DEFAULT now())"""

    book_author = f"""
        CREATE TABLE book_auth(
            book_id INT REFERENCES book(book_id),
            author_id INT REFERENCES author(author_id),
            last_update TIMESTAMP DEFAULT now())"""

    category = f"""
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            last_update TIMESTAMP DEFAULT now())"""

    book_category = f"""
        CREATE TABLE book_category(
            book_id INT REFERENCES book(book_id),
            category_id INT REFERENCES category(category_id),
            last_update TIMESTAMP DEFAULT now())"""

    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            category_id INT REFERENCES category(category_id),
            last_update TIMESTAMP DEFAULT now())"""

    customer = f"""
        CREATE TABLE customer(
            customet_id SERIAL PRIMARY KEY,
            first_name VARCHAR(25),
            last_name VARCHAR(25),
            phone_number VARCHAR(12),
            last_update TIMESTAMP DEFAULT now())"""


    staff = f"""
            CREATE TABLE staff(
                staff_id SERIAL PRIMARY KEY,
                first_name VARCHAR(25),
                last_name VARCHAR(25),
                phone_number VARCHAR(12),
                address_id INT REFERENCES address(address_id)
                last_update TIMESTAMP DEFAULT now())"""

    rental = f"""
        CREATE TABLE rental(
            rental_id SERIAL PRIMARY KEY,
            customer_id INT REFERENCES customer(customer_id),
            book_id INT REFERENCES book(book_id),
            start_date DATE,
            returned_date DATE,
            staff_if INT REFERENCES staff(staff_id),
            last_update TIMESTAMP DEFAULT now())"""


    payment = f"""
            CREATE TABLE payment(
                payment_id SERIAL PRIMARY KEY,
                rental_id INT REFERENCES rental(rental_id),
                amount NUMERIC(8, 2),
                staff_if INT REFERENCES staff(staff_id),
                last_update TIMESTAMP DEFAULT now())"""


    tables = {"book": book,
              "author": author,
              "book_author": book_author,
              "category": category,
              "book_category": book_category,
              "address": address,
              "customer": customer,
              "staff": staff,
              "rental": rental,
              "payment": payment}

    for table, query in tables.items():
        print(table + Database.connect(query))


if __name__ == "__main__":
    create_table()
