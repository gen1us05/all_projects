n = input("-->")
mytuple = (12, 23, "olma", "nok")

mytuple = list(mytuple)

mytuple.remove(n)

mytuple = tuple(mytuple)

print(mytuple)
