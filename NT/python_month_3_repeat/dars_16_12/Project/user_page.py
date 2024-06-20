from python_month_3_repeat.dars_16_12.Project import working_files


def user(username, password):

    print("User page \n-----------------------")

    menu = input("""
    1.Kurslar ro'yxatini ko'rish
    2.O'zim haqimdagi ma'lumotlarni ko'rish
    3.Log Out
    
    ---> """)
    while menu != "1" and menu != "2" and menu != "3":
        print("Bunday buyruq mavjud emas")
        menu = input("--->")
    if menu == "1":
        return working_files.kurslar_royxat(username, password, status="user")
    elif menu == "2":
        return working_files.oz_malumot(username, password, status="user")
    elif menu == "3":
        return working_files.log_out(username, password)


