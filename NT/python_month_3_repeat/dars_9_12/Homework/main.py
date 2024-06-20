import json


def cours_list():
    with open("course_list.json", "r") as f:
        data = json.load(f)
        for course in data["corse"]:
            print("akurslar royxati")
            print(f"""
                name: {course['name']}
                description: {course['description']}
                modules_count: {course['modules_count']}
                active_students: {course['active_students']}
                create_data: {course['create_data']}
                """)

        back = input("Orqaga qaytish--> back")
        while back == "back":

            print("Bunday komanda mavjud emas")
            back = input("Orqaga qaytish--> back")
            if back == "back":
                return user_port()


def admin_port():
    menu = int(input("""
            USER
           1. Kurslar ro'yxatini ko'rish
           2. O'zim haqimdagi ma'lumotlarni ko'rish
           3. Kursga yozilish
           4. Log Out
           >>> """))
    if menu == 1:
        pass
    elif menu == 4:
        return main()


def user_port():
    menu = int(input("""
        ADMIN
        1. Kurslar ro'yxatini ko'rish
        2. O'zim haqimdagi ma'lumotlarni ko'rish
        3. Kursga yozilish
        4. Log Out
        >>> """))
    if menu == 1:
        return cours_list()
    elif menu == 2:
        pass
    elif menu == 4:
        return main()

def main():
    username = input("username: ")
    password = input("password: ")
    with open("users.json", "r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                if int(i["role"]) == 0:
                    return admin_port()
                else:
                    return user_port()

    print("Username yoki parol xato kiritildi")
    return main()


def person_data():
    with open("users.json", "r") as file:
        data = json.load(file)


if __name__ == '__main__':
    main()
