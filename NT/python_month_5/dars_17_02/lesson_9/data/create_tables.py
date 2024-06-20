import time
from datetime import datetime
from base import Database

def create():
    book = """
        CREATE TABLE book(
            book_id SERIAL PRIMARY KEY,
            title VARCHAR(20),
            price FLOAT,
            created_date TIMESTAMP DEFAULT now());
    """

    author = """
            CREATE TABLE author(
                author_id SERIAL PRIMARY KEY,
                first_name VARCHAR(20),
                last_name VARCHAR(20),
                birth_date DATE,
                created_date TIMESTAMP DEFAULT now());
        """


    book_author = """
        CREATE TABLE book_author(
            book_author_id SERIAL PRIMARY KEY,
            book_id INT REFERENCES book(book_id),
            author_id INT REFERENCES author(author_id))
    """

    book_clone = """
            CREATE TABLE book_clone(
                book_clone_id SERIAL PRIMARY KEY,
                title VARCHAR(20),
                price FLOAT,
                created_date TIMESTAMP DEFAULT now());
        """


    data_tables = {
        # "book": book,
        # "author": author,
        # "book_author": book_author,
        "book_clone": book_clone
    }

    for i in data_tables:
        time.sleep(3)
        print(f"Database {i} + {Database.connect(data_tables[i], "create")}")


if __name__ == "__main__":
    print(datetime.now().time())
    create()
    print(datetime.now().time())
