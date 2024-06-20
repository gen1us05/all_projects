import csv
import json
import os

def cours_list():
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
                return user_port()


def user_port():
    os.system("color 2")
    menu = int(input("""
        1. Kurslar ro'yxatini ko'rish
        2. O'zim haqimdagi ma'lumotlarni ko'rish
        3. Kursga yozilish
        4. Log Out
        >>> """))

    if menu == 1:
        return cours_list()
    elif menu == 2:
        pass


def admin_port():
    menu = int(input("""
           1. Kurslar ro'yxatini ko'rish
           2. O'zim haqimdagi ma'lumotlarni ko'rish
           3. Kursga yozilish
           4. Log Out
           >>> """))

def main():
    username = input("username:")
    password = input("password:")
    with open("users.csv", encoding="utf-8") as file:
        data = csv.reader(file, delimiter=";")

        for i in data:
            if i[2] == username and i[3] == password:
                if int(i[4]) == 0:
                    return user_port()
                else:
                    return admin_port()

    print("Username yoki password xato kiritildi")
    return main()


if __name__ == "__main__":
    main()