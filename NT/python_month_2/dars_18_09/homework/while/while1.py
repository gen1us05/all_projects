a, b = map(int, input().split())

s = 0
i = b
while i < a + 1:
    i += b
    s += b
d = a - s
print(d)

# while a > b:
#     a -= b
# print(a)
