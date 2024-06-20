from base import Database

def city():
    query = f"""CREATE TABLE city(
    city_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    last_update DATE DEFAULT now());
"""
    Database.connect("localhost", "dorixona", "postgres", "password", query)


def address():
    query = f"""CREATE TABLE address(
    address_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    city_id INT REFERENCES city(city_id),
    last_update DATE DEFAULT now());
"""
    Database.connect("localhost", "dorixona", "postgres", "password", query)

def table3():
    query = f"""CREATE TABLE dorixona(
    dorixona_id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    address_id INT REFERENCES address(address_id),
    work_start VARCHAR(10),
    work_end VARCHAR(10));
"""
    Database.connect("localhost", "dorixona", "postgres", "password", query)


def table4():
    query = f"""CREATE TABLE firma(
    firma_id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    address_id INT REFERENCES address(address_id),
    phone VARCHAR(20));
"""
    Database.connect("localhost", "dorixona", "postgres", "password", query)


def staff():
    query = f"""CREATE TABLE staff(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    birth_year INT NOT NULL,
    dorixona_id INT REFERENCES dorixona(dorixona_id),
    address_id INT REFERENCES address(address_id),
    phone VARCHAR(20));
"""
    Database.connect("localhost", "dorixona", "postgres", "password", query)


def product_t():
    query = f"""CREATE TABLE product(
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    count INT,
    price INT,
    start_date DATE DEFAULT NOW(),
    end_date DATE,
    firma_id INT REFERENCES firma(firma_id),
    description TEXT);
    """
    Database.connect("localhost", "dorixona", "postgres", "password", query)

def dorixona_p():
    query = f"""CREATE TABLE dorixona_product(
        product_id INT REFERENCES product(product_id),
        dorixona_id INT REFERENCES dorixona(dorixona_id),
        last_update DATE DEFAULT NOW());
        """
    Database.connect("localhost", "dorixona", "postgres", "password", query)


def pay_type():
    query = f"""CREATE TABLE pay_type(
        pay_type_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        last_update DATE DEFAULT NOW());
        """
    Database.connect("localhost", "dorixona", "postgres", "password", query)

def payment():
    query = f"""CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amount INT NOT NULL,
            dorixona_id INT REFERENCES dorixona(dorixona_id),
            product_id INT REFERENCES product(product_id),
            staff_id INT REFERENCES staff(staff_id),
            pay_type_id INT REFERENCES pay_type(pay_type_id),
            pay_time DATE DEFAULT NOW());
            """
    Database.connect("localhost", "dorixona", "postgres", "password", query)



if __name__=="__main__":
    payment()

