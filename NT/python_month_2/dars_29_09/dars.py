# n = input("-->")
# # b = n.lower()
# # d = {}
# # for i in n:
# #     d[i] = n.count(i)
# # print(d)
#
# d = {i: n.count(i) for i in n if i != " "}
#
# print(d)


a = int(input("-->"))

x = "Dushanba" if a == 1 else \
    "Seshanba" if a == 2 else \
        "Chorshanba" if a == 3 else \
            "Payshanba" if a == 4 else \
                "Juma" if a == 5 else \
                    "Shanba" if a == 6 else \
                        "Yakshanba" if a == 7 else "bunday hafta kuni yoq"

print(x)
