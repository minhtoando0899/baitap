'''Write a Python program to create a list reflecting the run-length encoding
from a given list of integers or a given list of characters.
'''
# from itertools import groupby
# def encode_list(s_list):
#     return [[len(list(group)), key] for key, group in groupby(s_list)]
# n_list = [1,1,2,3,4,4.3,5, 1]
# print("Original list:")
# print(n_list)
# print("\nList reflecting the run-length encoding from the said list:")
# print(encode_list(n_list))
# n_list = 'automatically'
# print("\nOriginal String:")
# print(n_list)
# print("\nList reflecting the run-length encoding from the said string:")
# print(encode_list(n_list))
from itertools import groupby


class Reflecting:
    def __init__(self, list):
        self.list = list

    def ref(self):
        return [[len(list(group)), key] for key, group in groupby(self.list)]


R1 = Reflecting([1, 1, 2, 3, 4, 4.3, 5, 1])
R1.ref()
print("Original list:")
print(R1.list)
print("List reflecting the run-length encoding from the said list:")
print(R1.ref())
