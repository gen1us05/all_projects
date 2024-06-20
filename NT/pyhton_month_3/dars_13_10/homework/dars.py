#
# a = 23
#
#
# class Person:
#     ism = "ali"
#     familiya = "valiyev"
#     yosh = 18
#
#     def toliq_ism(self):
#         return f"{self.ism} {self.familiya}"
#
#
# p1 = Person()
# print(p1.ism)
# print(p1.toliq_ism())
#
# p3 = Person()
# p3.ism = "hoshimjon"
# print(p3.toliq_ism())
#

class Room:
    def __init__(self, length: float, width: float, height: float, cr: str):
        self.length = length
        self.width = width
        self.height = height
        self.color = cr

    def maydon(self):
        return self.length * self.width

    def hajm(self):
        return self.height * self.maydon()

    def info(self):
        return f"Rangi:{self.color}, Maydon:{self.maydon()}, Hajm:{self.hajm()}"


if __name__ == '__main__':
    b = float(input("Boyi: "))
    e = float(input("Eni: "))
    h = float(input("Balandligi: "))
    c = input("Rangi: ")
    r1 = Room(h, e, b, c)
    print("xonaning yuzasi: ", r1.maydon())
    print("Honaning hajmi: ", r1.hajm())
    print("Hona malumotlari: ", r1.info())
