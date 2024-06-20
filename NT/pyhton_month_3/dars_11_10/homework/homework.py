import os
import pprint
from collections import defaultdict
from pprint import pprint

os.chdir("dars3")

data = defaultdict(list)
for file in os.listdir():
    name, type = file.split(".")
    data[type].append(name)
pprint(dict(data))
