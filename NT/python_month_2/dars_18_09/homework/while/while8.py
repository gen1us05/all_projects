n = int(input())

i = 0
s = 0
while i < n + 1:
    if i ** 2 <= n:
        s = i
    i += 1
print(s)
