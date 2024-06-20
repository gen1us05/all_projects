import json
from datetime import datetime
import os
import function
import admin_page
import user_page

def add_kurs(username, password):
    l = [username, password]
    """yangi kurs qoshish"""
    class Courses:
        def __init__(self, name, description, modules_count, price, active_students, create_date=None):
            self.name = name
            self.description = description
            self.__modules_count = modules_count
            self.price = price
            self.__active_students = active_students
            self.__create_date = datetime.today()

        def get_modules_count(self):
            return self.__modules_count

        def save(self):
            new_course = {
                "name": self.name,
                "description": self.description,
                "modules_count": self.__modules_count,
                "price": self.price,
                "active_students": self.__active_students,
                "create_date": f"{datetime.today()}",

            }
            with open("kurs.json") as file:
                data = json.load(file)
            data['course'].append(new_course)
            with open("kurs.json", "w") as f:
                json.dump(data, f, indent=6)
            print("muvaffaqiyatli qo'shildi")

        def __str__(self):
            return f"{self.name}"

    name = (input("nomi:"))
    description = input("izohi:")
    modules_count = input("modullar:")
    price = int(input("narxi:"))
    active_students = 0
    curs = Courses(name, description, modules_count, price, active_students)
    curs.save()
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)



def add_member(username, password):
    """kursga yozilish"""
    with open("kurs.json", "r") as f:
        dat = json.load(f)
        print("kurslar royxati:")
        for i in dat['course']:
            print(i["name"])

    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                x = int(i["balance"])
                print(x)

    nom = input("kurs nomini kiriting:")
    for i in range(len(dat['course'])):
        if dat['course'][i]["name"] == nom:
            x = x- int(dat['course'][i]["price"])
            if x >= 0:
                dat['course'][i]["active_students"] = int(dat['course'][i]["active_students"]) + 1
                print("kursga qoshildingiz")

    with open("kurs.json", "w") as file:
        json.dump(dat, file, indent=6)

    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                i["balance"] = x

    with open("users.json", "w") as file:
        json.dump(data, file, indent=6)
    back = input("Ortga qaytish: (back)")

    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")

    if back == "back":
        os.system("color 3")
        os.system("cls")
        return user_page.user_p(username, password)
