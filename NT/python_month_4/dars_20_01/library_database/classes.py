from datetime import datetime

class Book:
    def __init__(self, name: str, description: str, count:int, language, amount):
        self.name = name
        self.description = description
        self.count = count
        self.language = language
        self.amount = amount
        self.create_date = f"{datetime.now().date()}"

    def __str__(self):
        return f"{self.name, self.amount}"



