# n = int(input("-->"))
#
# # l = []
# # for i in range(10, n+1, 10):
# #     l.append(i)
# #
# # t = tuple(l)
#
# t = (i for i in range(10, n + 1, 10))
#
# print(tuple(t))
#
#


import json

with open("todos.json") as f:
    data = json.load(f)
c, d = 0, 0
for i in data:
    if i["completed"]:
        c += 1
    else:
        d += 1

print(c)
print(d)
