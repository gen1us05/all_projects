import csv
import json

d1 = {}
d2 = {}
# with open("regions.csv", "r") as f:
    # for i in csv.DictReader(f):
        # print(i)
with open("districts.csv") as file:
    for j in csv.DictReader(file):
        # d1[j] = j["region"]
        for row in j:
            print(row.ite)





# if j["region"] == d1:
#     print(j["region"])

#         # print(f"regions.csv: {i['п»їid']}")
# with open("districts.csv") as f:
#     # for j in csv.DictReader(f):
#     # print(f"districts.csv: {j['region']}")
#     if i["п»їid"] == j["region"]:
#         print(i)
#
# # # "п»їid"

# import csv
# import json
#
# male = []
# female = []
# with open("people.csv") as f:
#     data = list(csv.DictReader(f))
#     for row in data:
#         if row["gender"] == "Male":
#             male.append(row)
#         elif row["gender"] == "Female":
#             female.append(row)
#
# with open("male.json", "w") as f:
#     json.dump(male, f, indent=4)
#
# with open("female.json", "w") as f:
#     json.dump(female, f, indent=4)