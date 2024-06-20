from math import  floor

r1 = int(input("aylana radiusini kiriting r1:"))
r2 = int(input("aylana radiusini kiriting r2:"))


p = int(floor(3.14))

s1 = p * r1 * r1
s2 = p * r2 * r2
s3 = p * (r1-r2)


print(s1, s2, s3)

