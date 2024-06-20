
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return f" ism: {self.first_name} \n familya: {self.last_name}"


shaxs = Student("John", "Doe")

print(shaxs.full_name())


