n = int(input())

i = 1
while i < n + 1:
    if n == (2 ** i):
        print(i)
        i += 1
    else:
        i += 1
