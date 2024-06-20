a, b = map(int, input().split())

s = 0
i = b
while i < a + 1:
    i += b
    s += 1
print(s)
