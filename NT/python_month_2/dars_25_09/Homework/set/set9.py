n = input("-->")
mytuple = (12, 23, "olma", "nok")

mytuple = list(mytuple)

mytuple.append(n)

mytuple = tuple(mytuple)

print(mytuple)