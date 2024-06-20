from dars10.exceptions import BadRequestException, OkException, NotFoundException


def check_username_unique(users: list, username: str):
    for user in users:
        if user["username"] == username:
            raise BadRequestException(f"{username} is already taken")
    return True
def check_user_exists(users:list, id):
    for user in users:
        if user["id"] == id:
            return 200

    return 404
