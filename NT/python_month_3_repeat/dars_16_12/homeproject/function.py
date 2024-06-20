import csv
import json
from datetime import datetime
import os
from mainproject import main
import admin_page
import user_page


def users(username, password):

    """userlarni korish"""

    print("sayt foydalanuvchilari")
    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            print(i["firstname"], i["lastname"])

    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)

def kurslara(username, password):

    """admin uchun kurslar royxati"""

    with open("kurs.json", 'r') as file:
        data = json.load(file)
        print("Kurslar ro'yxati: ")
        for course in data['course']:
            print(f"""
                name: {course['name']}
                izoh: {course['description']}
                modullar: {course['modules_count']}
                narxi: {course['price']}
                talabalar: {course['active_students']}
                yaratildi: {course['create_date']}
                    """)
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return admin_page.admin_p(username, password)


def kurslarf(username, password):

    """user uchun kurslar"""

    with open("kurs.json", 'r') as file:
        data = json.load(file)
        print("   Kurslar ro'yxati: ")
        for course in data['course']:
            print(f"name: {course['name']}\nizoh: {course['description']}\nmodullar: {course['modules_count']}\nnarxi: {course['price']}\nyaratildi: {course['create_date']}\n\n")
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return user_page.user_p(username, password)

def profil(username, password):

    """profil malumotlarini korish"""

    print("Profil malumotlari")

    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == str(password):
                print(f"ismi : {i['firstname']} \nfamiliyasi : {i['lastname']} \nusername : {i['username']} \npassword : {i['password']}\nmablagi={i['balance']}")
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        with open("users.json", "r") as file:
            data = json.load(file)
            for i in data["users"]:
                if i["username"] == username and i["password"] == password:
                    if i["status"] == 1:
                        return admin_page.admin_p(username, password)
                    else:
                        return user_page.user_p(username, password)


def maps(username, password):

    """filiallar joylashuvi"""

    with open("maps.txt", "r") as fl:
        z = fl.read()
        print(z)
    back = input("Ortga qaytish: (back)")
    while back != "back":
        os.system("color 6")
        print("Bunday buyruq mavjud emas namunaga etibor bering")
        back = input("Orqaga qaytish: (back)")
    if back == "back":
        os.system("color 3")
        os.system("cls")
        return user_page.user_p(username, password)

def logout(username, password):
    """akkountdan chiqish"""
    username = False
    password = False
    # print(username, password)
    return main()

