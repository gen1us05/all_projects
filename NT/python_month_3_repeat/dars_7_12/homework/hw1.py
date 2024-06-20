import csv

# with open("file.txt", "w") as f:
#     for i in range(11):
#         f.write("Hello Files \n")


#  3
file = []
with open("hospital.csv", encoding='utf-8') as f:
    for i in csv.reader(f, delimiter=';'):
        file.append(i)
mx = []
for i, j in file:
    mx.append(j)
del mx[0]
x = []
for i in range(3):
    x.append(max(mx))
    mx.remove(max(mx))


for i, j in file:
    for k in x:
        if k == j:
            print(i, j)
