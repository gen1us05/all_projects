class Room:
    def __init__(self, boyi: int, eni: int, balandligi: int, rangi: str):
        self.boyi = boyi
        self.eni = eni
        self.balandligi = balandligi
        self.rangi = rangi

    def info(self):
        return f" Boyi {self.boyi} eni {self.eni} balandligi {self.balandligi} rangi {self.rangi}"


if __name__ == '__main__':
    boyi = int(input("boyi -->  "))
    eni = int(input("eni -->  "))
    balandlik = int(input("balandligi -->  "))
    rangi = input("rangi -->  ")

    s1 = Room(boyi, eni, balandlik, rangi)

    print(s1.info())

