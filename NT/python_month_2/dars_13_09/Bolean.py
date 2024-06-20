# #  Bolean
#
# a = int(input("a soni: "))
# b = int(input("b soni: "))
#
# c = a % 2 == 1 or b % 2 == 1
#
# print(c)

from math import pi

r1, r2, r3 = map(int, input().split())

s1 = pi * r1 ** 2
s2 = pi * r2 ** 2
s3 = pi * r3 ** 2

print(f"{s1:.2f} {s2:.2f} {s3:.2f}")
