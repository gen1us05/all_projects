n = int(input())

i = 0
c = 1
d = 0
while i < n:
    if i ** 2 > n:
        if c == 1:
            d = i
            c += 1
    i += 1

print(d)

# qisqartirishga harakar qlib koraman