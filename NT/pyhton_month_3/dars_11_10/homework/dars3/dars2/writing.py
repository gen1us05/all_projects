"""
Assalomu Alaykum
Saralangan kitoblar
Yulduzlar mangu yonadi
Qorda gullagan daraxt
Shirin Qovunlar Mamlakati
Mehrobdan Chayon
tugadi
"""
lines = []
qator = input()
while qator != "tugadi":
    lines.append(qator)
    qator = input()

text = "\n".join(lines)
text += "\n"
# print(text)
with open("books.txt", "w") as f:
    f.write(text)
