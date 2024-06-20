import requests

d = []
for _ in range(5):
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    # print(data["length"])
    d.extend(data["fact"].split())

print(d)
print(len(d))
