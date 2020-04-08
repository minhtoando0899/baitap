# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter


class Combine:
    def __init__(self, dic_1, dic_2):
        self.dic_1 = dic_1
        self.dic_2 = dic_2

    def com(self):
        new_dic = Counter(self.dic_1) + Counter(self.dic_2)
        print(new_dic)


C1 = Combine({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400})
C1.com()