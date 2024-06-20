a, b = map(int, input().split())

s = 0
for i in range(b - 1, a, -1):
    print(i)
    s = s + 1
print(s)
