

class Avto:
    model = "chevrolet"


    def __init__(self, rang, price):
        self.color = rang
        self.price = price

    def func(self):
        return self.color


    @classmethod
    def method(cls):
        return cls('qora', '15000')


nexia = Avto.method

print(nexia.color)

