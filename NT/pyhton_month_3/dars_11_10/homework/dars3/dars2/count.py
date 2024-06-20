import csv
c={}
with open("sorted_people.csv", "r") as f:
    for row in csv.DictReader(f):
        c[row["country"]] = c.get(row["country"], 0)+1
with open("statistics.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Counrtry", "People"])
    for v in c.items():
        # print(v)
        writer.writerow(v)



