myset = {"olma", "anor", 12, 34, 45, True, False}
mycars = {"matiz", "damas", "cabalt", "nexia", "olma"}

myset = list(myset)
mycars = list(mycars)

myset.extend(mycars)

myset = set(myset)

newset = myset.symmetric_difference(mycars)

print(newset)
