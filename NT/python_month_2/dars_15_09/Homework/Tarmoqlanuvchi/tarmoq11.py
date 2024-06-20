x, y, z = map(float, input().split())

min = x

if min > y:
    min = y
if min > z:
    min = z

m = min
if x < 1 and y < 1 and z < 1:
    w = x + y + z - min
    min = w / 2

if m == x:
    print(min, y, z)
elif m == y:
    print(x, min, z)
else:
    print(x, y, min)
