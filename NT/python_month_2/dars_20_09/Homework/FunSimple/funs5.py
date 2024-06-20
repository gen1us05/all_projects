def RectPC(x1, y1, x2, y2):
    p1 = (x1 + y1) * 2
    s1 = x1 * y1
    p2 = (x2 + y2) * 2
    s2 = x2 * y2
    print(f"perimetrlar {p1, p2}")
    print(f"perimetrlar {s1, s2}")


RectPC(23, 12, 4, 6)
