from base import Database

def insert():
    query = f"""
    INSERT INTO payment(amount,kurs_id,user_id,pay_type_id)
     VALUES(120,1,1,2);
     """

    Database.connect("localhost", "kurs", "postgres", "password", query)


if __name__ == "__main__":
    insert()
