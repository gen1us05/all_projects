import json
from datetime import datetime
import os
import function
import models

def admin_p(username, password):

    """admin sahifasi"""

    print("Admin sahifasi")
    menu = input("""
    1.Kurslar ro'yxati
    2.Foydalanuvchilar 
    3.Yangi kurs qoshish
    4.Profil malumotlari
    5.chiqish
    """)

    if menu == '1':
        return function.kurslara(username, password)
    elif menu == '2':
        return function.users(username, password)
    elif menu == '3':
        return models.add_kurs(username, password)
    elif menu == '4':
        return function.profil(username, password)
    elif menu == '5':
        return function.logout(username, password)
    else :
        print("bunday buyruq yo'q qayta kiriting")
        return admin_p(username, password)

