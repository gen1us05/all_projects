a, b = map(int, input().split())

s = 1
for i in range(a, b + 1, 1):
    s = s * i
print(s)
