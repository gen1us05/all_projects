n = int(input())

s1 = 0
for i in range(1, n+1, 2):
    c = 10 + i
    d = c / 10
    s1 = s1 + d
s2 = 0
for i in range(2, n+1, 2):
    c = 10 + i
    d = c / 10
    s2 = s2 - d

x = s1 + s2
print(f"{x:.2f}")
