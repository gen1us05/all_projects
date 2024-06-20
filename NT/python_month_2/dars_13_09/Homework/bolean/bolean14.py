a = int(input("birinchi sonni kiriting:"))
b = int(input("ikkinchi sonni kiriting:"))
c = int(input("uchinchi sonni kiriting:"))

d = a % 2 == 0 and b % 2 == 1 and c % 2 == 1 or a % 2 == 1 and b % 2 == 0 and c % 2 == 1 or a % 2 == 1 and b % 2 == 1 and c % 2 == 0

print(d)
