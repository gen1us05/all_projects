from base import Database


def create_table():
    gorod = f"""
        CREATE TABLE gorod(
            gorod_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            description VARCHAR(255))"""

    filials = f"""
        CREATE TABLE filials(
            filial_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            gorod_id INT REFERENCES gorod(gorod_id),
            google_location VARCHAR(55))"""

    location = f"""
        CREATE TABLE location(
            location_id SERIAL PRIMARY KEY,
            filial_id INT REFERENCES filials(filial_id),
            gorod_id INT REFERENCES gorod(gorod_id),
            google_location VARCHAR(55))"""

    teachers = f"""
        CREATE TABLE teachers(
            teacher_id SERIAL PRIMARY KEY,
            first_name VARCHAR(25),
            last_name VARCHAR(25),
            email VARCHAR(40))"""

    groups = f"""
        CREATE TABLE groups(
            group_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            teacher_id INT REFERENCES teachers(teacher_id),
            location_id INT REFERENCES location(location_id))"""

    kourse = f"""
        CREATE TABLE kourse(
            kourse_id SERIAL PRIMARY KEY,
            name VARCHAR(35),
            lesson_duration VARCHAR(55),
            lesson_price SMALLINT,
            group_id INT REFERENCES groups(group_id))"""

    users = f"""
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(35),
            last_name VARCHAR(35),
            email VARCHAR(25),
            kourse_id INT REFERENCES kourse(kourse_id),
            group_id INT REFERENCES groups(group_id)) """

    payment = f"""
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            kourse_id INT REFERENCES kourse(kourse_id),
            user_id INT REFERENCES users(user_id),
            payment_type VARCHAR(25))"""


    tables = {
        "gorod": gorod,
        "filials": filials,
        "location": location,
        "teachers": teachers,
        "group": groups,
        "kourse": kourse,
        "users": users,
        "payment": payment
    }

    for table, query in tables.items():
        print(table + Database.connect(query))

if __name__ == '__main__':
    create_table()