from base import Database

def insert():
    query = f"""INSERT INTO users(first_name, last_name, email) VALUES('John', 'Doe', 'johndoe23@gmail.com')"""
    Database.connect(query)

if __name__ == '__main__':
    insert()