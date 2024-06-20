


# class CloneRange:
#     def __init__(self, start, stop=None, step=1):
#         if stop is None:
#             self.stop = start
#             self.start = -step
#             self.step = step
#         else:
#             self.start = start - step
#             self.stop = stop
#             self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += self.step
#         if self.start >= self.stop:
#             raise StopIteration
#         return self.start
#
#
# for i in CloneRange(2,25,3):
#     print(i)



def example():
    yield 1
    yield 3
    yield 4
    yield 6
    yield 8

if __name__ == "__main__":
    for i in example():
        print(i)