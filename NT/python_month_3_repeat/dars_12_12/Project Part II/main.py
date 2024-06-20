import csv
import user_port
from admin import admin_port

def main():
    username = input("username:")
    password = input("password:")
    with open("users.csv", encoding="utf-8") as file:
        data = csv.reader(file, delimiter=";")

        for i in data:
            if i[2] == username and i[3] == password:
                if int(i[4]) == 0:
                    return user_port.user_port(username, password)
                else:
                    return admin_port(username, password)

    print("Username yoki password xato kiritildi")
    return main()

if __name__ == "__main__":
    main()