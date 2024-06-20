# for i in range(100):
#     if i % 5 != 0 and i % 7 != 0:
#         print(i)

#
# for i in range(10):
#     print(f"{i} ning kvadrati:{i ** 2}")


# k, n = map(int, input().split())
#
# for i in range(0, n, 1):
#     print(k)


# k = int(input("konfet narxi: "))
# S = 0
# for i in range(1, 11):
#     S = S + k
#     print(i, "kg konfet narxi", S)


# k = int(input("konfet narxi: "))
# for i in range(10, 21, 2):
#     print(f"{i / 10} kg konfet narxi: {i*k}")

# s = 0
# for i in range(1, 100, 2):
#     s = s + i
# print(s)


# a = int(input("son kiriting: "))
# s = 0
# for i in range(1, a + 1, 1):
#     if a % i == 0:
#         s += 1
# if s == 2:
#     print("tub son")
# else:
#     print("bu son tub emas", s)


# a = int(input("son kiriting: "))
# i = a + 1
# while i > 0:
#     i -= 1
#     print(i)


a = int(input())
s = 0
i = 1
while i < a + 1:
    if i % 7 == 0:
        s += i
    i += 1
print(s)
