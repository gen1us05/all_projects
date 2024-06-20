def InvertDigit(a, b, c):
    m = 1
    n = 10
    x1 = 0
    x2 = 0
    x3 = 0
    s = 1
    for i in range(m, n):
        if a > m and a < n:
            x1 = s
        if b > m and b < n:
            x2 = s
        if c > m and c < n:
            x3 = s
        if x1 == 0 or x2 == 0 or x3 == 0:
            m *= 10
            n *= 10
            s += 1
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(x1):
        q = a % 10
        a = a // 10
        s1 = s1 * 10 + q
    for i in range(x2):
        q = b % 10
        b = b // 10
        s2 = s2 * 10 + q
    for i in range(x3):
        q = c % 10
        c = c // 10
        s3 = s3 * 10 + q
    print(s1, s2, s3)


InvertDigit(12132, 132, 3214)
