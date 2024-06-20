n = int(input())

s = 1
for i in range(1, n, 1):
    c = 10 + i
    d = c / 10
    s = s * d
print(f"{s:.2f}")
