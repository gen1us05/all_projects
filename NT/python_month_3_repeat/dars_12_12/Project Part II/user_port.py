import csv
import json
import os
from main import main
import admin


def course_list(username, password, key=None):
    with open("course_list.json", 'r') as file:
        data = json.load(file)
        for course in data["course"]:
            print("Kurslar ro'yxati")
            print(f"""
                name: {course['name']}
                description: {course['description']}
                modules_count: {course['modules_count']}
                active_students: {course['active_students']}
                create_date: {course['create_date']}
                """"")

        back = input("Orqaga qaytish: (back)")
        while back != "back":
            os.system("color 4")

            print("Bunday command mavjud emas")
            back = input("Orqaga qaytish: (back)")
            if back == "back":
                os.system("color 2")
                os.system("cls")
                if key == "user":
                    return user_port(username, password)
                if key == "admin":
                    return admin.admin_port(username, password)
        if back == "back":
            os.system("color 2")
            os.system("cls")
            if key == "user":
                return user_port(username, password)
            if key == "admin":
                return admin.admin_port(username, password)


def user_info(username, password):
    with open("users.csv", encoding="utf-8") as file:
        data = csv.reader(file, delimiter=";")
        for user in data:
            if user[2] == username and user[3] == password:
                print(f"""
                First Name: {user[0]}
                Last Name: {user[1]}
                Username: {user[2]}
                Password: {user[3]}
                Status: User
                """)
        back = input("Orqaga qaytish: (back)")
        while back != "back":
            os.system("color 4")
            print("Bunday command mavjud emas")
            back = input("Orqaga qaytish: (back)")
        if back == "back":
            os.system("color 2")
            os.system("cls")
            return user_port(username, password)


def enrol(username, password):
    with open("course_list.json", 'r') as file:
        data = json.load(file)
        count = len(data["course"])
    print("Kurslar ro'yxati")
    for t in range(1, count+1):
        print(f"{t} - {data['course'][t-1]['name']}")
    course_id = int(input("O'qimoqchi bo'lgan kursingizni tartib raqamini tanlang:"))
    while course_id not in list(range(1, count + 1)):
        print("Bunday kurs mavjud emas")
        course_id = int(input("O'qimoqchi bo'lgan kursingizni tartib raqamini tanlang:"))
    with open("user_course.csv", "a") as file:
        course = data['course'][course_id-1]['name']
        username = username
        file.write(f"{username};{course}\n")
    print("Successful")
    return user_port(username, password)


def user_port(username, password):
    os.system("color 2")
    print("User Port")
    menu = int(input("""
        1. Kurslar ro'yxatini ko'rish
        2. O'zim haqimdagi ma'lumotlarni ko'rish
        3. Kursga yozilish
        4. Log Out
        >>> """))

    if menu == 1:
        return course_list(username, password, key='user')

    elif menu == 2:
        return user_info(username, password)

    elif menu == 3:
        return enrol(username, password)

    elif menu == 4:
        return main()

    else:
        print("Bunday service mavjud emas")
        return user_port(username, password)


