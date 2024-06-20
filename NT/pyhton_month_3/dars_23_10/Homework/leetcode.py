# 1. 1678

# class Solution:
#     def interpret(self, command: str) -> str:
#
#         return command.replace("(al)", "al").replace("()", "o")
#


# 2. 1773

# class Solution:
#     def countMatches(self, items, ruleKey, ruleValue):
#
#         ans = 0
#         for t in items:
#             if ruleKey == "type" and t[0] == ruleValue:
#                 ans += 1
#             elif ruleKey == "color" and t[1] == ruleValue:
#                 ans += 1
#             elif ruleKey == "name" and t[2] == ruleValue:
#                 ans += 1
#         return ans


# 3. 1704

# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         vowels = "aeiouAEIOU"
#         return sum(c in vowels for c in s[:len(s) // 2]) == sum(c in vowels for c in s[len(s) // 2:])


# 4. 412
#
# class Solution:
#     def fizzBuzz(self, n):
#
#         ans = []
#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 ans.append("FizzBuzz")
#             elif i % 3 == 0:
#                 ans.append("Fizz")
#             elif i % 5 == 0:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i))
#         return ans


