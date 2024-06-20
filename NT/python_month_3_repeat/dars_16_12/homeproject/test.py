import json
from datetime import datetime

class User:
    def __init__(self, firstname, lastname, username, password, status, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.status = status
        self.balance = balance

    def get_balance(self):
        return self.balance

    def save(self):
        new_user = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "password": self.password,
            "status": self.status,
            "balance": self.balance,

        }
        with open("users.json", "r") as file:
            data = json.load(file)
        data["users"].append(new_user)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=6)
        print("muvaffaqiyatli qo'shildi")

    def __str__(self):
        return f"{self.firstname}"


firstname = input("ismi:")
lastname = input("familiyasi:")
username = input("username:")
password = input("paroli:")
status = int(input("status:"))
balance = int(input("mablag'i:"))
z = User(firstname, lastname, username, password, status, balance)
z.save()
