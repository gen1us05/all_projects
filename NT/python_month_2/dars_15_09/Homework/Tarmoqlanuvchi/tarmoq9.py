x, y = map(float, input().split())

if x < y:
    x = (x + y) / 2
    y = (x * 2) * (y * 2)
else:
    y = (x + y) / 2
    x = (x * 2) * (y * 2)

print(f"{x:.1f} {y:.1f}")

