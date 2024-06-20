from pprint import pprint


class Note:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Note(new_data)
        new_node.next = self.head
        self.head = new_node


    def append(self, new_data):
        new_node = Note(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Xato!!!")
        new_node = Note(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

a1 = Note(1)
a2 = Note(5)
a3 = Note(45)

ll = LinkedList()
ll.head = a3
a3.next = a1
a1.next = a2
ll.append(101)

data = list(range(1, 50))
a1 = Note(data[0])
ll = LinkedList()
ll.head = a1
for i in data[1:]:
    new_node = Note(i)
    last = ll.head
    while last.next:
        last = last.next
    last.next = new_node
pprint(type(ll))
