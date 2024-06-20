x, y, z = map(float, input().split())

max = x
min = x

if max < y:
    max = y
elif max < z:
    max = z

if min > y:
    min = y
elif min > z:
    min = z

min = min ** 2

print(f"{max:.2f} {min:.2f}")
