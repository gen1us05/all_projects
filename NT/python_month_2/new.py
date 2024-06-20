# Variant
# B
#
# 1 - savol

# a1, a2 = map(str, input("yosh va ismni kiriting: ").split())
# b1, b2 = map(str, input("yosh va ismni kiriting: ").split())
#
# if a1 > b1:
#     print(b2)
# else:
#     print(a2)

# 2 - savol

# n = str(input("--> "))
# s = []
# for i in n:
#     d = i.upper()
#     if i == d:
#         s.append(i)
# print(s)
# print(len(s))

# 3 - savol

# n = str(input("--> "))
#
# l = []
#
# for i in n:
#     i = int(i)
#     if i == 4:
#         i = 7
#     elif i == 7:
#         i = 4
#     l.append(i)
# s = 0
# for i in l:
#     for j in range(1):
#         s *= 10
#         s += i
# print(s)

# 4 - savol

# n = int(input("--> "))
#
# d = {}
#
# for i in range(1, n + 1):
#     d[i] = i * 2
#
# print(d)

# 5 - savol
#
# n1 = map(str, input("son kiriting: ").split(","))
# n2 = map(str, input("son kiriting: ").split(","))
# l1 = []
# l2 = []
#
# for i in n1:
#     l1.append(i)
# for i in n2:
#     l2.append(i)
#
# l1 = set(l1)
# l2 = set(l2)
#
# s = l1.symmetric_difference(l2)
#
# s = list(s)
# s.sort()
# s.reverse()
# print(s)
