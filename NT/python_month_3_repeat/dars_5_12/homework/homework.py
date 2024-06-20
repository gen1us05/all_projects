from datetime import datetime

class User:
    def __init__(self, username: str, password: str, create_time=None):
        self.username = username
        self.__password = password
        self.create_time = f"{datetime.today()}"

    def get_password(self):
        return self.__password

    def set_password(self, new_password: str):
        if len(new_password) >= 8 and self.__password != new_password and new_password[0] == new_password[0].title():
            self.__password = new_password
        else:
            print("Siz murakkabroq password kiritishingiz kerak")

    def login(self):
        return f"Login with {self.username}"

    def logout(self):
        return f"Logout with {self.username}"

    def __str__(self):
        return f"{self.username}"


class Teacher(User):
    def __init__(self, first_name, last_name, username, password, login, logout):
        User.__init__(self, username, password, create_time=None)
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.logout = logout

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username}"


class Assistend(Teacher):
    def __init__(self, first_name, last_name, username, password, group):
        Teacher.__init__(self, first_name, last_name, username, password)
        self.group = group

    def help_task(self):
        return f"Help task with Assistend. First name {self.first_name}"

    def check_task(self):
        return f"Check task with Assistend. First name {self.first_name}"


class Mentor(Assistend):
    def __init__(self, first_name, last_name, username, password, group, status_exam: bool):
        Assistend.__init__(self, first_name, last_name, username, password, group)
        self.__status_exam = status_exam

    def get_status_exam(self):
        return self.__status_exam

    def set_status_exam(self, status):
        if isinstance(status, bool):
            self.__status_exam = status
        else:
            print("Siz faqat TRUE yoki FALSE kiritishingiz kerak")

    def help_task(self):
        return f"Help task with Mentor. First name {self.first_name}"

    def check_task(self):
        return f"Check task with Mentor. First name {self.first_name}"

    def deploying_task(self):
        return f"Deploying task with Mentor. First name {self.first_name}. Deploying time {datetime.today()}"

    def deploying_video(self):
        return f"Deploying video with Mentor. First name {self.first_name}. Deploying time {datetime.today()}"


foydalanuvchi = User("user1", "pass123")
foydalanuvchi_1 = User("fakeuser", "pass123")
foydalanuvchi_2 = User("user2", "pass123")

print(foydalanuvchi.create_time)
print(foydalanuvchi_1.get_password())
print(foydalanuvchi_2.get_password())



