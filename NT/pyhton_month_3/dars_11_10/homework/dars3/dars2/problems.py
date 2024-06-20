# #algo63
# def factorial(n: int) -> int:
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     return s
#
#
# if __name__ == '__main__':
#     summa = 0
#     n = int(input())
#     ishora = 1
#     for i in range(1, 2 * n, 2):
#         summa += 1 / factorial(i) * ishora
#         ishora *= -1
#     print(f"{summa:.4f}")

# 63 79
# algo79
# from math import pi, cos
# a = int(input())
# x = -pi / 2
# s = 0
# h = pi / 19
#
# while x <= pi:
#     s += pow(a, a / 3) + x ** 2 *cos(a * x)
#     x += h
#
# print(f"{s:.2f}")


# algo 92
from math import cos, log

x, y, a, b = map(int, input().split())
S, P, SP = 0, 1, 0

for u in range(1, x + 1):
    S += (u ** 2 + 2 * u) / (u ** 3 + u * cos(u) ** 2 + 1)

for m in range(1, y + 1):
    P *= (m ** 2 + 1) / (m ** (3 / m) + 2)

for i in range(1, a + 1):
    K = 1
    for k in range(1, b + 1):
        K *= log((k ** i + k ** (1 / i))/ (k ** 3 + i ** (1 / k)))
    SP += K

print(f"{S:.2f} {P:.2f} {SP:.2f}")
