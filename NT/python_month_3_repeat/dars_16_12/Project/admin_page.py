import json

from python_month_3_repeat.dars_16_12.Project import working_files


def admin(username, password):
    print("Admin page \n-------------------------------------")
    menu = input("""
    1.Kurslar ro'yxatini ko'rish
    2.O'zim haqimdagi ma'lumotlarni ko'rish
    3.Userlardi ko'rish
    4.Log Out
    
    ---> """)
    while menu != "1" and menu != "2" and menu != "3" and menu != "4":
        print("Bunday buyruq mavjud emas")
        menu = input("--->").lower()
    if menu == "1":
        return working_files.kurslar_royxat(username, password, status="admin")
    elif menu == "2":
        return working_files.oz_malumot(username, password, status="admin")
    elif menu == "3":
        return working_files.users(username, password, status="admin")
    elif menu == "4":
        return working_files.log_out(username, password)

def kourse(username, password):
    print("""\n
    1.Kurslarni o'zgartirish
    2.Yangi kurs qoshish
    Orqaga qaytish --> back
    """)
    menu = input("---> ")
    while menu != "back" and menu != "1" and menu != "2":
        print("Bunday buyruq mavjud emas")
        menu = input("---> ")
    if menu == "back":
        return admin(username, password)
    elif menu == "1":
        return working_files.edit_courses(username, password)
    elif menu == "2":
        return working_files.add_kourse(username, password)
    else:
        print("Nomalum xato!!!")

def user_edit(username, password):
    with open("users.json", "r") as f:
        data = json.load(f)

    print("\nO'zgartirmoqchi bolgan userni kiriting\n")
    user = input("username --> ")

    for i in data["users"]:

        if i["username"] == user and i["status"] == 1:
            print("\n1.Admin malumotlarini o'zgartirish")
            print("2.Adminlikni olib tashlash\n")
        elif i["username"] == user and i["status"] == 0:
            print("\n1.User malumotlarini o'zgartirish")
            print("2.Admin qilib tayinlash\n")

    print("Orqaga qaytish --> back")

    menu = input("---> ")
    while menu != "back" and menu != "1" and menu != "2":
        print("Bunday buyruq mavjud emas")
        menu = input("---> ")
    if menu == "back":
        return user_edit(username, password)
    elif menu == "1":
        return working_files.user_edits(username, password, user)
    elif menu == "2":
        return working_files.change_status(username, password, user)
    else:
        print("Nomalum xato!!!")

