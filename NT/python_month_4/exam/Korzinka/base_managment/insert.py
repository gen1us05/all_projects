from base import Database

def insert():
    query = f"""INSERT INTO product(name, expiration_date, price, count) VALUES('soat', '2020-03-11', 150, 50)"""
    Database.connect(query)
if __name__ == '__main__':
    insert()