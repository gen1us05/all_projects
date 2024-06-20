a, b, c = map(int, input().split())

if a <= b and b <= c:
    a = a + a
    b = b + b
    c = c + c
else:
    if a < 0:
        a = -a + (-a)
    elif b < 0:
        b = -b + (-a)
    elif c < 0:
        c = -c + (-a)

print(a, b, c)
