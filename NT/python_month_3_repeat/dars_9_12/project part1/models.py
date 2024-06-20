from datetime import datetime


class Courses:
    def __init__(self, name, description, modules_count, price, active_students, create_date=None):
        self.name = name
        self.description = description
        self.__modules_count = modules_count
        self.price = price
        self.__active_students = active_students
        self.__create_date =  datetime.today()

    def get_modules_count(self):
        return self.__modules_count

    def __str__(self):
        return f"{self.name}"

class Speciality:
    def __init__(self, name, count_course, create_date=None):
        self.name = name
        self.count_course = count_course
        self.create_date = datetime.today()

    def __str__(self):
        return f"{self.name} {self.count_course} {self.create_date}"

class Users:
    def __init__(self, first_name, last_name, username, password, status):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password
        self.__status = status

    def get_password(self):
        return self.__password

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username}"

