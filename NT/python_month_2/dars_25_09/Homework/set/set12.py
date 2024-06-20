mylist = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
d = []
for i in mylist:
    i = list(i)
    del i[-1]
    i.append(100)
    i = tuple(i)
    d.append(i)
print(d)

