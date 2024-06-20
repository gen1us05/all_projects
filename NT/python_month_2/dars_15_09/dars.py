# a = int(input("son kiriting: "))
#
# if a > 0:
#     a = a + 2
#
# else:
#     a = a - 1
#
# print(a)
#


a, b, c = map(int, input().split())

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("son xato kiritilgan")
