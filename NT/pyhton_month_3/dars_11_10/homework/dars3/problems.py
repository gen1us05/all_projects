# homework 2 3
# import requests
# import csv
#
# path = 'https://jsonplaceholder.typicode.com/albums'
# response = requests.get(path)
# data = {}
# for row in response.json():
#     data[row['userId']] = data.get(row['userId'], 0)+1
# data[1]+=2
# data[5]+=6
# data[7]+=3
# data[6]-=4
# data[10]+=16
# print(data)
# print(data.items())
# data = sorted(data.items(), key=lambda x:x[1], reverse=True)
# # task2.csv
# columns = ["agentID", 'albumCount']
# with open("task2.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(columns)
#     for row in data:
#         writer.writerow(row)
import csv
from pprint import pprint

# data = dict(data)
# print(data)

#homework 3

# /home/ravshanjon/NT/module3/statistics.csv
# countries:list = []
# with open("statistics.csv" ) as f:
#     for row in csv.DictReader(f):
#         row["People"] = int(row["People"])
#         countries.append(row)
#
# d = sorted(countries, key=lambda x: x["People"], reverse=True)
# pprint(d)