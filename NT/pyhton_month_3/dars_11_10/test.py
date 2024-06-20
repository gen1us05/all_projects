import os
os.chdir('pass')

for file in os.listdir():
    # if os.path.isdir(file) and file not in exclude:
        with open(file, 'r') as f:
            d = f.read()
