n = int(input())

i = 1
c = 1
d = 0
while i < n + 1:
    if 3 ** i > n:
        if c == 1:
            d = i
            c += 1
    i += 1

print(d)

# qisqartirishga harakar qlib koraman
