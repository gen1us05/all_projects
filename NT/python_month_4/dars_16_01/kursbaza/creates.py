from base import Database

def city():
    query = f"""CREATE TABLE city(
    city_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    last_update DATE DEFAULT now());
"""
    Database.connect("localhost", "kurs", "postgres", "password", query)


def address():
    query = f"""CREATE TABLE address(
    address_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    city_id INT REFERENCES city(city_id),
    last_update DATE DEFAULT now());
"""
    Database.connect("localhost", "kurs", "postgres", "password", query)

def user():
    query = f"""CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL, 
    birth_year INT NOT NULL,
    address_id INT REFERENCES address(address_id),
    phone VARCHAR(20),
    created_time DATE DEFAULT NOW());
"""
    Database.connect("localhost", "kurs", "postgres", "password", query)

def lesson():
    query = f"""CREATE TABLE lesson(
    lesson_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    decription TEXT,
    homework TEXT,
    create_time DATE DEFAULT NOW());
    """
    Database.connect("localhost", "kurs", "postgres", "password", query)


def modules():
    query = f"""CREATE TABLE modules(
    modul_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    lesson_id INT REFERENCES lesson(lesson_id),
    create_time  DATE DEFAULT NOW());
    """
    Database.connect("localhost", "kurs", "postgres", "password", query)


def kurs():
    query = f"""CREATE TABLE kurs(
    kurs_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    modul_id INT REFERENCES modules(modul_id),
    create_time DATE DEFAULT NOW());"""

    Database.connect("localhost", "kurs", "postgres", "password", query)

def group():
    query = f"""CREATE TABLE groups(
    kurs_id INT REFERENCES kurs(kurs_id),
    users INT REFERENCES users(user_id));"""

    Database.connect("localhost", "kurs", "postgres", "password", query)


def pay_type():
    query = f"""CREATE TABLE pay_type(
        pay_type_id SERIAL PRIMARY KEY,
        type VARCHAR(20),
        last_update DATE DEFAULT NOW());
        """
    Database.connect("localhost", "kurs", "postgres", "password", query)

def payment():
    query = f"""CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amount INT NOT NULL,
            kurs_id INT REFERENCES kurs(kurs_id),
            user_id INT REFERENCES users(user_id),
            pay_type_id INT REFERENCES pay_type(pay_type_id),
            pay_time DATE DEFAULT NOW());
            """
    Database.connect("localhost", "kurs", "postgres", "password", query)




if __name__ == "__main__":
    payment()