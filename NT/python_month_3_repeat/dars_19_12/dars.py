#
#
# yangi = map(str, input("-->").split(" "))
#
# for c in yangi:
#     while c != "back" and c != "1" and c != "2" and c != "3" and c != "4" and c != "5":
#         print("Bunday buyruq mavjud emas")
#         yangi = map(str, input("O'zgartiriladigan qismni probel orqali yozing -->").split(" "))
#
#     if c == "back":
#         pass
#     elif c == "1":
#         print("Name changed successfully")
#     elif c == "2":
#         print("Description changed successfully")
#     elif c == "3":
#         print("Modules_count changed successfully")
#     elif c == "4":
#         print("Price changed successfully")
#     elif c == "5":
#         print("Active_students changed successfully")
#     else:
#         print("Aniqlanmagan xato !!!")

import time
from datetime import datetime

x = datetime.today()
print(x)