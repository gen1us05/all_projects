from math import sqrt


def MEAN(a, b, c, d):
    x = (a + b) / 2
    y = (a + c) / 2
    z = (a + d) / 2
    print(f"O'rta arifmetrigi : {x, y, z}")
    x = sqrt(a * b)
    y = sqrt(a * c)
    z = sqrt(a * d)
    print(f"O'rta geometrigi : {x:.2f} {y:.2f} {z:.2f}")


MEAN(23, 12, 4, 5)
