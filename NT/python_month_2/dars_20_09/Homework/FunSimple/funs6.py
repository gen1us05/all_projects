def DigitCountSum(a, b, c):
    y = a + b + c
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
    print(f"a= {x1} xonali")
    print(f"b= {x2} xonali")
    print(f"c= {x3} xonali")
    print(f"yigindi {y}")


DigitCountSum(12, 123, 125134)
