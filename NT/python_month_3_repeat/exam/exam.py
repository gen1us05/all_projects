#  OneTech

# degree -- daraja




class Degree:

    def degrees(self, degree_name):
        if degree_name == 'web dasturlash':
            print("Degree: web dasturlash")
            print("Degree is full stack")
            print("Degree is middle")
            print("Degree is senior")


class Student:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree


class Lessons:
    def __init__(self, name, time, specialty):
        self.name = name
        self.time = time
        self.specialty = specialty

    def lessons(self, lesson_name):
        if lesson_name != self.name:
            print("Lesson does not found")
        else:
            print("Lesson")
            print("lesson name is " + self.name)
            print("lesson time is " + self.time)
            print("lesson specialty is " + self.specialty)

    def add_lesson(self, lesson_name, lesson_time, lesson_specialty):
        if lesson_name != self.name:
#           bu yerda bazaga yuklanadi
            print("Lesson is successfully added")



class User:

    def __init__(self, first_name, last_name, username, password, courses, old, degree, status, experiense):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.courses = courses
        self.old = old
        self.degree = degree
        self.__status = status
        self.__password = password
        self.experience = experiense

    def user_info(self, first_name, last_name, username, courses, old, degree, experiense):
        print(f"First name -------> {first_name}")
        print(f"Last name --------> {last_name}")
        print(f"Username ---------> {username}")
        print(f"User courses -----> {courses}")
        print(f"User young -------> {old}")
        print(f"User degree ------> {degree}")
        print(f"User experience --> {experiense}")

    def  create_admin(self):
        if self.__status != "admin":
            self.__statusstatus == "admin"
            print("Changed successfully")
        else:
            print("This user is an admin")


    def delete_admin(self):
        if self.__status == "admin":
            self.__statusstatus == "user"
            print("Changed successfully")
        else:
            print("This user is not admin")

    def change_password(self, old_password, new_password):
        if old_password == self.__password and old_password != new_password:
            self.__password = new_password





