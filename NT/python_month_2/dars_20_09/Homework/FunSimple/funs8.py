def AddRightDigit(son, raqam):
    m = 1
    n = 10
    x1 = 0
    s = 1
    c = son
    for i in range(m, n):
        if raqam > m and raqam < n:
            x1 = s
        if x1 == 0:
            m *= 10
            n *= 10
            s += 1
    for i in range(x1):
        c = c * 10
        i += 1
    javob = c + raqam
    print(javob)


AddRightDigit(123, 12)
