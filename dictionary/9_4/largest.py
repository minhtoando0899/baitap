# Write a Python program to find the highest 3 values in a dictionary.
# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest)
from heapq import nlargest


class Largest:
    def __init__(self, dic):
        self.dic = dic

    def lar(self):
        three_largest = nlargest(3, self.dic, key=self.dic.get)
        print(three_largest)


L1 = Largest({'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20})
L1.lar()
