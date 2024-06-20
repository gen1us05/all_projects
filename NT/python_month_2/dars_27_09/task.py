d = {
    'emp1': {'name': 'Bob', 'job': 'mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Dev'}
}

for i in d.values():
    for d in i.get('name'):
        print(d)

