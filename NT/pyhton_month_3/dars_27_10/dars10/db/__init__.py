import json

from dars10.exceptions import NotFoundException
from dars10.models import User


class AuthorizationRepo:
    """
        crud -> create read update delete
    """

    def __init__(self, file):
        self.file = file
        self.__get_data()

    def __get_data(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(self.file, "w") as f:
                data = []
                json.dump(data, f, indent=3)
        self.users = data

    def __commit(self):
        with open(self.file, "w") as f:
            json.dump(self.users, f, indent=3)

    def create_user(self, user: dict):
        self.users.append(user)
        self.__commit()

    def delete_user(self, id: str):
        for user in self.users:
            if user["id"] == id:
                self.users.remove(user)
                self.__commit()
                return
        raise NotFoundException(message=f" Not found such  {id} user ")

    def find_user_by_username(self, username: str) -> User:
        for user in self.users:
            if user["username"] == username:
                return User(**user)
        raise NotFoundException(message=f"Non Exist such username in db")


class TransferRepo:
    def __init__(self, file):
        self.file = file

    def __get_data(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(self.file, "w") as f:
                data = []
                json.dump(data, f, indent=3)
        self.transfers = data

    def __commit(self):
        with open(self.file, "w") as f:
            json.dump(self.transfers, f, indent=3)

    def add_balance(self, user: User, amount: float):
        pass


__all__ = ["AuthorizationRepo", "TransferRepo"]
