n = int(input("butun son kiriting: "))
a = float(input("xoxlagan sonni kiriting: "))

for i in range(1, n+1, 1):
    s=a**i
    print(f"{s:.2f}")
