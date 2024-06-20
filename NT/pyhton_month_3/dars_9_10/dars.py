# with open("data.txt", "r") as f:
#     d = f.read()
#
# s = []
# e = {}
# for i in d:
#     s.append(i)
#     e[i] = s.count(i)
#
# print(e)


# lines = []
# qator = input()
#
# while qator != "tugadi":
#     lines.append(qator)
#     qator = input()
#
# text = "\n".join(lines)
# text += "\n"
#
# with open("books.txt", "a") as f:
#     f.write(text)


import csv
from pprint import pprint

data: list[dict] = []

with open("people.csv", "r") as f:
    for r in csv.DictReader(f):
        data.append(r)

sorted_data = sorted(data, key=lambda x: x["country"])

with open("sorted_people.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(list(sorted_data[0].keys()))
    for row in sorted_data:
        writer.writerow(list(row.values()))
