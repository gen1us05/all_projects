d = {1: 1, 2: 4, 3: 9, 4: 16, 10: 100, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

s = d.pop(1)

for i in d.values():
    if s < i:
        s = i

print(s)
