"""
special/magic/dunder  methods
"""


# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.x * self.y
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __lt__(self, other):
#         return self.area() > other.area()
#
#     def __gt__(self, other):
#         return self.area() < other.area()
#
#
# if __name__ == "__main__":
#     p1 = Shape(12, 24)
#     p2 = Shape(13, 24)
#
# print(p1 == p2)
# print(p1 < p2)
# print(p1 > p2)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return -self.x + other.x, -self.y + other.y


if __name__ == "__main__":
    k = Vector(4, 5)
    v = Vector(12, 2)

    print(k + v)
