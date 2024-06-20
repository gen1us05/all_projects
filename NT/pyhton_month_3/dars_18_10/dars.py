# x, y = map(int, input().split())
# mat = []
# for _ in range(x):
#     row = list(map(int, input().split()))
#     mat.append(row)
# sums = []
# mx, mn = max(mat[0]), min(mat[0])
# for w in mat:
#     rx, rn = max(w), min(w)
#     if mx < rx:
#         mx = rx
#     if mn > rn:
#         mn = rn
#     sums.append(sum(w))
# print(*sums)
# print(mx, mn)


"""

4 6
71 27 -63 45 4 -24
21 -37 41 -47 16 -48
87 26 -69 55 89 -58
20 49 -21 36 80 -58

"""




######################



# class Employee:
#     email = "test@gmail.com"  # class attributes
#     _phone = "+9989112345678"

#     def __init__(self, fullname: str, salary: float):
#         if isinstance(fullname, str):
#             self.fullname = fullname  # object attributes
#         else:
#             raise ValueError("Full Name must be string")
#         if isinstance(salary, float):
#             self.salary = salary  # object attributes
#         else:
#             raise ValueError("Salary must be float")

#     def __str__(self):
#         return f"{self.fullname}, {self.salary}, {self.email}, {self._phone}"
    
    
#     @classmethod
#     def update_phones(str, phone):
#         if phone[0]=="+" and phone[1:]...
#         cls._phone = phone
            
    



class boy:

    def __init__(self, color:str):
        self.color = color
        s = []
        for i in color.split(" "):
            s.append(i)
        print(f"Boy used {s} colrs")

if __name__ == '__main__':

    p1 = boy("red green yellow")
