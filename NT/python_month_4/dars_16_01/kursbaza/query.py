from base import Database

def sorov():
    query = f"""SELECT 
    users.user_id,
    users.first_name,
    groups.kurs_id,
    groups.users
    FROM users
    INNER JOIN groups
    ON users.user_id = groups.users;"""

    Database.connect("localhost", "kurs", "postgres", "password", query)

if __name__ == "__main__":
    sorov()