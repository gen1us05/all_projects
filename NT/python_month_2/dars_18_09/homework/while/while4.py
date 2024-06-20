# n = int(input())
#
# s = 0
# i = 3
# while i < n + 1:
#     i += 3
#     s += 3
# d = n - s
# if d == 0:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")


n = int(input("-->:"))
a = 1
while a < n:
    a *= 3
if a == n:
    print(True)
else:
    print(False)
