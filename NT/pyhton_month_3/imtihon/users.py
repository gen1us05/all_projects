import json


class Users:
    def __init__(self):
        self.file = "users.json"
        self.__get_data()

    def __get_data(self):
        try:
            with open(self.file, "r") as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []

    def __commit(self):
        with open(self.file, "w") as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, full_name, username, email, password):
        self.users.append({
            "full_name": full_name,
            "username": username,
            "email": email,
            "password": password
        })
        self.__commit()
        print("added")

    def login(self, username, password):
        for user in self.users():
            if username == self.users["username"] and password == self.users["password"]:
                print("accept")
            else:
                print("x")


def main_menu():
    b = Users()
    while True:
        print()
        print("login -------------1")
        print("register ----------2")
        n = input()

        match n:
            case "1":
                username = input("username: ")
                password = input("password")
                b.login(username, password)
            case "2":
                full_name = input("full_name: ")
                username = input("username: ")
                email = input("email")
                password = input("password")
                b.add_user(full_name, username, email, password)


if __name__ == '__main__':
    main_menu()
