n = input("-->")
mycars = {"matiz", "damas", "cabalt", "nexia", "olma"}
mycars = list(mycars)
for i in mycars:
    if i == n:
        mycars.remove(n)

mycars = set(mycars)

print(mycars)
