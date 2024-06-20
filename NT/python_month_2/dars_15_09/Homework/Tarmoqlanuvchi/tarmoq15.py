a, b, c = map(float, input().split())

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + (D * (1 / 2))) / (2 * a)
    x2 = (-b - (D * (1 / 2))) / (2 * a)
    print(f"{x1:.2f} {x2:.2f}")
elif D == 0:
    x = -((b) / (2 * a))
    print(f"{x:.2f}")
else:
    print("NO")
