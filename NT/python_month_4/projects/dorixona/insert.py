from base import Database

def insert():
    query = f"""INSERT INTO pay_type(name) VALUES('naqd')"""
    Database.connect('localhost', 'dorixona', 'postgres', 'password', query)

if __name__ == '__main__':
    insert()