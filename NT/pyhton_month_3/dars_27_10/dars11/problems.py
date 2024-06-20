from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        for i, word in enumerate(sentences):
            sentences[i] = word.split()
        print(len(max(sentences, key=len)))


if __name__ == '__main__':
    o = Solution()
    o.mostWordsFound(["w jrpihe zsyqn l dxchifbxlasaehj",
                      "nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom",
                      "xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg",
                      "krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm",
                      "rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr",
                      "o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk",
                      "hrvh efqvjilibdqxjlpmanmogiossjyxepotezo",
                      "qstd zui nbbohtuk",
                      "qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"])
