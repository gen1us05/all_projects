n, k = map(int, input().split())

s = 0
c = 0
i = k
while i < n + 1:
    i += k
    s += k
    c += 1
d = n - s
print(f"butun:{c} qoldiq:{d}")
