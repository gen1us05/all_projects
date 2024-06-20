a, b, c, d = map(float, input().split())

min = a
max = a

if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d

if a <= b and b <= c and c <= d:
    a = max
    b = max
    c = max
    d = max
else:
    a = min
    b = min
    c = min
    d = min

print(a, b, c, d)


