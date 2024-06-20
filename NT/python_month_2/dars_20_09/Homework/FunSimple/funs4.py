from math import sqrt


def Triangle(a, b, c):
    if a == b and b == c:
        p = a * 3
        print(f"perimetri : {p}")
        s = ((sqrt(3)) / (4)) * a ** 2
        print(f"Yuzasi : {s:.2f}")
    else:
        print("kiritilgan sondan teng tomonli uchburchak yasab bolmaydi")


Triangle(12, 12, 12)
