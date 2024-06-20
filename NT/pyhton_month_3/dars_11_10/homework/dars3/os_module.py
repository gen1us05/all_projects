"""
 listdir -> fayl va papkalar royhatini qaytaradi
 chdir -> papkaga kirish
"""
import os

os.chdir('../dars2')
mx: int = 0
f = ''
for file in os.listdir():
    # with open(file, 'r') as f:#relative path
    with open(f"{os.getcwd()}/{file}", 'r') as f:  # absolute path
        data = f.read()
        if mx < len(data):
            f = os.getcwd()
            mx = len(data)
print(mx)
print(f.name)