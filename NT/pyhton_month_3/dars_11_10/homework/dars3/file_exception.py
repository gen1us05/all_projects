
# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("nolga bo'lish mumkin emas")
try:
    with open("data.txt") as f:
        f.read()
    import django
except FileNotFoundError:
    print("File Topilmadi")
except ImportError:
    print("Xato Import Qilindi")
for i in range(5):
    print(i)