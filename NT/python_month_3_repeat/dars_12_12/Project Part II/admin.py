import user_port
import csv
import os
from models import Courses
import json


def admin_info(username, password):
    with open("users.csv", encoding="utf-8") as file:
        data = csv.reader(file, delimiter=";")
        for user in data:
            if user[2] == username and user[3] == password:
                print(f"""
                First Name: {user[0]}
                Last Name: {user[1]}
                Username: {user[2]}
                Password: {user[3]}
                Status: Admin
                """)
        back = input("Orqaga qaytish: (back)")
        while back != "back":
            os.system("color 4")
            print("Bunday command mavjud emas")
            back = input("Orqaga qaytish: (back)")
        if back == "back":
            os.system("color 2")
            os.system("cls")
            return admin_port(username, password)

def add_course():
    print("Yangi kurs qo'shish")
    name = input("name: ")
    description = input("description: ")
    modules_count = input("modules_count: ")
    course = Courses(name, description, modules_count, 50)
    course.save()



def admin_port(username, password):
    print("Admin Port")
    menu = int(input("""
           1. Kurslar ro'yxatini ko'rish
           2. O'zim haqimdagi ma'lumotlarni ko'rish
           3. Yangi kurs qo'shish
           4. Log Out
           >>> """))

    if menu == 1:
        return user_port.course_list(username, password, key="admin")

    elif menu == 2:
        pass

    elif menu == 3:
        return add_course()

    elif menu == 4:
        pass
