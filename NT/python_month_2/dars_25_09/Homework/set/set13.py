mylist = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
d = []
for i in mylist:
    if len(i) != 0:
        d.append(i)

print(d)
