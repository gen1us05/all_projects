from typing import List

#  leetcode  14. Longest Common Prefix
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#           return ' "" '
#
#         for i in range(len(strs[0])):
#           for j in range(1, len(strs)):
#             if i == len(strs[j]) or strs[j][i] != strs[0][i]:
#               return strs[0][:i]
#
#         return strs[0]
#
# x = Solution.longestCommonPrefix(self=0, strs=["flower","flow","flight"])
#
# print(x)


#   leetcode  20. Valid Parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#
#         for c in s:
#             if c == '(':
#                 stack.append(')')
#             elif c == '{':
#                 stack.append('}')
#             elif c == '[':
#                 stack.append(']')
#             elif not stack or stack.pop() != c:
#                 return False
#
#         return not stack
#
# x = Solution.isValid(self=0,s="(]")
# print(x)