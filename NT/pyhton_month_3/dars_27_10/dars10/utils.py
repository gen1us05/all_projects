"""
menu - > cyan
error -> red
succes -> green
info -> blue
"""
from hashlib import sha256
from uuid import uuid4

from colorama import Fore, Style
from bcrypt import hashpw, checkpw, gensalt


def generate_id() -> str:
    return str(uuid4())


def print_menu(s: str):
    print(Fore.CYAN, s, Style.RESET_ALL)


def print_error(s: str):
    print(Fore.RED, s, Style.RESET_ALL)


def print_succes(s: str):
    print(Fore.GREEN, s, Style.RESET_ALL)


def print_info(s: str):
    print(Fore.BLUE, s, Style.RESET_ALL)


def hashpassword(password: str) -> str:
    salt = gensalt()
    p = password.encode("utf-8")
    return hashpw(p, salt).decode("utf-8")


def matchpassword(password: str, hashed_password) -> bool:
    return True if checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")) else False

# if __name__ == '__main__':
# print(generate_id())
# hashed_password = hashpassword("!@#$%")
# print(matchpassword("!@#$%", hashed_password))
# s1 = (sha256("#24".encode("utf-8")))
# print(s1.hexdigest())
