a = int(input("uch xonali son kiriting: "))

x1 = a % 10
x2 = a // 10 % 10
x3 = a // 100

b = x1 != x2 and x2 != x3 and x1 != x3

print(b)
