import json

from python_month_3_repeat.dars_16_12.Project import admin_page, user_page


def main():
    username = input("username -->")
    password = input("password -->")

    with open("users.json", "r") as f:
        data = json.load(f)
        for i in data['users']:
            if i["username"] == username and i["password"] == password:
                if i["status"] == 1:
                    return admin_page.admin(username, password)
                else:
                    return user_page.user(username, password)
        else:
            print("\nUsername yoki parol xato\n")
            return main()


if __name__ == '__main__':
    main()