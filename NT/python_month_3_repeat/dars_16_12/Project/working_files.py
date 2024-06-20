import json
from datetime import datetime

from python_month_3_repeat.dars_16_12.Project import admin_page, user_page
from python_month_3_repeat.dars_16_12.Project.main import main


def kurslar_royxat(username, password, status):
    with open("kurses.json", "r") as f:
        data = json.load(f)
        for i in data["course"]:
            print("\n")
            print(f"Course name --> {i['name']}")
            print(f"Description --> {i['description']}")
            print(f"Modules_count --> {i['modules_count']}")
            print(f"Price --> {i['price']}")
            if status == "admin":
                print(f"Active students --> {i['active_students']}")
                print(f"Create date --> {i['create_date']}")
        if status == "admin":
            return admin_page.kourse(username, password)
        else:
            return back(username, password, status)


def back(username, password, status):
    back = input("\norqaga qaytish --> back\n--->").lower()
    while back != "back":
        print("Bunday buyruq mavjud emas")
        back = input("\norqaga qaytish --> back\n--->").lower()
    if back == "back":
        if status == "admin":
            return admin_page.admin(username, password)
        else:
            return user_page.user(username, password)


def oz_malumot(username, password, status):
    with open("users.json", "r") as f:
        data = json.load(f)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                print(f"Firstname --> {i['firstname']}")
                print(f"Lastname --> {i['lastname']}")
                print(f"Username --> {i['username']}")
                print(f"Password --> {i['password']}")
                if i["status"] == 1:
                    print(f"Status --> admin")
                else:
                    print(f"Status --> user")
                print(f"Balance --> {i['balance']}")

        return back(username, password, status)


def users(username, password, status):
    with open("users.json", "r") as f:
        data = json.load(f)
        for i in data["users"]:
            print("\n")
            print(f"Firstname --> {i['firstname']}")
            print(f"Lastname --> {i['lastname']}")
            print(f"Username --> {i['username']}")
            print(f"Password --> {i['password']}")
            if i["status"] == 1:
                print(f"Status --> admin")
            else:
                print(f"Status --> user")
            print(f"Balance --> {i['balance']}")

        return admin_page.user_edit(username, password)

def edit_courses(username, password):
    with open("kurses.json", "r") as f:
        data = json.load(f)
    edit = input("Course name --->")
    # while i["name"] != edit:
    #     print("Bunday kurs topilmadi")
    for i in data["course"]:

        if i["name"] == edit:
            print(f"\nName --> {i['name']}")
            print(f"Description --> {i['description']}")
            print(f"Modules_count --> {i['modules_count']}")
            print(f"Price --> {i['price']}")
            print(f"Active students --> {i['active_students']}")
            print(f"Create date --> {i['create_date']}")

            print("\n1.Name")
            print("2.Description")
            print("3.Modules_count")
            print("4.Price")
            print("5.Active_students")
            print("orqaga qaytish --> back\n")


            yangi = map(str, input("O'zgartiriladigan qismni yozing -->").split(" "))

            for c in yangi:

                while c != "back" and c != "1" and c != "2" and c != "3" and c != "4" and c != "5":
                    print("Bunday buyruq mavjud emas")
                    yangi = map(str, input("O'zgartiriladigan qismni probel orqali yozing -->").split(" "))

                if c == "back":
                    return admin_page.kourse(username, password)
                elif c == "1":
                    course_name = input("Course name --->")
                    i["name"] = course_name
                    print("Name changed successfully")
                elif c == "2":
                    description = input("Description --->")
                    i["description"] = description
                    print("Description changed successfully")
                elif c == "3":
                    modules_count = input("Modules_count --->")
                    i["modules_count"] = modules_count
                    print("Modules_count changed successfully")
                elif c == "4":
                    price = int(input("Price --->"))
                    i["price"] = price
                    print("Price changed successfully")
                elif c == "5":
                    active_students = input("active_students --->")
                    i["active_students"] = active_students
                    print("Active_students changed successfully")
                else:
                    print("Aniqlanmagan xato !!!")
            print("\n")
            print(f"Name --> {i['name']}")
            print(f"Description --> {i['description']}")
            print(f"Modules_count --> {i['modules_count']}")
            print(f"Price --> {i['price']}")
            print(f"Active students --> {i['active_students']}")
            print(f"Create date --> {i['create_date']}\n")

        with open("kurses.json", "w") as f:
            json.dump(data, f, indent=4)
            print("successfull")
        return admin_page.kourse(username, password)
        edit = input("Course name --->")

def add_kourse(username, password):
    with open("kurses.json", "r") as f:
        data = json.load(f)

    name = input("Course name -->")
    description = input("Course description -->")
    modules_count = input("Modules count -->")
    price = int(input("Price -->"))

    print(f"\nName --> {name}")
    print(f"Description --> {description}")
    print(f"Modules_count --> {modules_count}")
    print(f"Price --> {price}")

    chack = input("\nHammasi tog'rimi --> yes/no -->").lower()
    if chack == "yes":
        new_course = {
            "name": f"{name}",
            "description": f"{description}",
            "modules_count": f"{modules_count}",
            "price": f"{price}",
            "active_students": 0,
            "create_date": f"{datetime.today()}"
        }
        data["course"].append(new_course)
        with open("kurses.json", "w") as f:
            json.dump(data, f, indent=4)
            print("successfull")
            return admin_page.kourse(username, password)
    else:
        return admin_page.kourse(username, password)

def user_edits(username, password, user):
    with open("users.json", "r") as f:
        data = json.load(f)
    for i in data["users"]:
        if i["username"] == user:
            print(f"\n1.Firstname --> {i['firstname']}")
            print(f"2.Lastname --> {i['lastname']}")
            print(f"3.Username --> {i['username']}")
            print(f"4.Password --> {i['password']}")
            if i["status"] == 1:
                print(f"5.Status --> admin")
            else:
                print(f"5.Status --> user")
            print(f"6.Balance --> {i['balance']}")

            chack = map(str, input("O'zgartiriladigan qismni yozing -->").split(" "))

            for c in chack:

                while c != "back" and c != "1" and c != "2" and c != "3" and c != "4" and c != "5":
                    print("Bunday buyruq mavjud emas")
                    chack = map(str, input("O'zgartiriladigan qismni probel orqali yozing -->").split(" "))

                if c == "back":
                    return admin_page.user_edit(username, password)
                elif c == "1":
                    firstname = input("Firstname --->")
                    i["firstname"] = firstname
                    print("Firstname changed successfully")
                elif c == "2":
                    lastname = input("Lastname --->")
                    i["lastname"] = lastname
                    print("Lastname changed successfully")
                elif c == "3":
                    username_1 = input("Modules_count --->")
                    i["username"] = username_1
                    print("Username changed successfully")
                elif c == "4":
                    password_1 = int(input("Password --->"))
                    i["password"] = password_1
                    print("Password changed successfully")
                elif c == "5":
                    balance = input("Balance --->")
                    i["balance"] = balance
                    print("Active_students changed successfully")
                else:
                    print("Aniqlanmagan xato !!!")

            print(f"\n1.Firstname --> {i['firstname']}")
            print(f"2.Lastname --> {i['lastname']}")
            print(f"3.Username --> {i['username']}")
            print(f"4.Password --> {i['password']}")
            if i["status"] == 1:
                print(f"5.Status --> admin")
            else:
                print(f"5.Status --> user")
            print(f"6.Balance --> {i['balance']}")

    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
        print("Changed successfully")
    return admin_page.user_edit(username, password)

def change_status(username, password, user):
    with open("users.json", "r") as f:
        data = json.load(f)
    for i in data["users"]:
        if i["username"] == user and i["status"] == 1:
            tayinlash = input("Adminlik olinsinmi --> ok/no --> ")
            if tayinlash == "ok":
                i["status"] = 0
                print("Adminlik olib tashlandi!")
            else:
                return admin_page.user_edit(username, password)
        elif i["username"] == user and i["status"] == 0:
            tayinlash = input("Admin qilib tayinlash --> ok/no --> ")
            if tayinlash == "ok":
                i["status"] = 1
                print(i["status"])
                print("Admin qilib tayinlandi!")
            else:
                return admin_page.user_edit(username, password)
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
    return admin_page.user_edit(username, password)




def log_out(username, password):
    username = False
    password = False
    return main()