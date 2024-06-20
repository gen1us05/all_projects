import json
from datetime import datetime


class Courses():
    def __init__(self, name, description, modules_count, price, active_students=0, create_date=None):
        self.name = name
        self.description = description
        self.__modules_count = modules_count
        self.price = price
        self.__active_students = active_students
        self.__create_date = datetime.today()

    def __get_data(self):
        with open("course_list.json", "r") as f:
            self.course_list = json.load(f)

    def __commit(self):
        with open("course_list.json", "w") as f:
            json.dump(self.course_list, f, indent=4)

    def get_modules_count(self):
        return self.__modules_count

    def save(self):
        self.course_list.append({
            "name": self.name,
            "description": self.description,
            "modules_count": self.__modules_count,
            "price": self.price,
            "active_students": self.__active_students,
            "create_date": f"{datetime.today()}",
            "users": []
        })
        self.__commit()
        print("success")
        # new_course = {
        #     "name": self.name,
        #     "description": self.description,
        #     "modules_count": self.__modules_count,
        #     "price": self.price,
        #     "active_students": self.__active_students,
        #     "create_date": f"{datetime.today()}",
        #     "users": [],
        # }
        # with open("course_list.json", "a+") as file:
        #     data = json.load(file)
        #     file.write(data)
        #     data['course'].append(new_course)
        #     json.dump(data["course"], file)
        # print("successful")


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

    def add_user(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username}"

