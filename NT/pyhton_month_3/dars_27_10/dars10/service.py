from dars10.db import AuthorizationRepo, TransferRepo
from dars10.exceptions import UnauthorizedException, BadRequestException, NotFoundException, OkException
from dars10.models import User
from dars10.utils import print_info, hashpassword, matchpassword, print_succes
from dars10.validators import check_username_unique, check_user_exists


class AuthorizationService:
    def __init__(self, repo: AuthorizationRepo):
        self.repository = repo

    def login(self, username: str, password: str) -> User:
        user: User = self.repository.find_user_by_username(username=username)
        if matchpassword(password, user.password):
            return user
        else:
            raise BadRequestException("Your password or login is wrong ")

    def register(self, *args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        check_username_unique(self.repository.users, username)
        user = User(username=username, password=hashpassword(password), first_name=first_name, last_name=last_name)
        self.repository.create_user(user.__dict__)

    def delete_account(self, id: str):
        code = check_user_exists(self.repository.users, id)
        if code == 200:
            self.repository.delete_user(id)
            print_succes("user successfully deleted")
        else:
            raise NotFoundException(f"{id} id user Not Found")


class TransferService:
    def __init__(self, repo: TransferRepo):
        self.repository = repo

    def show_balance(self, session_user: User):
        print_info(f"Your balance is {session_user.balance}")

    def add_balance(self, user: User, amount: float):
        user.balance += amount
        print_info("Your balance ", user.balance)

    def transfer_money(self):
        print_info("Transfer Money Service")

    def transfer_history(self):
        print_info("Transfer History Service")


__all__ = ["AuthorizationService", "TransferService"]
