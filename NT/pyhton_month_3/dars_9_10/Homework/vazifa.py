with open("photos.json", "r") as f:
    d = f.read()

s = []

for i in d.split("}"):
    s.append(i)

s = set(s)
print(s)