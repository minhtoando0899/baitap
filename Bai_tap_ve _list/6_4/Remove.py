# # Write a Python program to remove consecutive duplicates of a given list.
# from itertools import groupby
# def compress(l_nums):
#     return [key for key, group in groupby(l_nums)]
# n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
# print("Original list:")
# print(n_list)
# print("\nAfter removing consecutive duplicates:")
# print(compress(n_list))
from itertools import groupby


class RemoveDuplicates:
    def __init__(self, list):
        self.list = list

    def rem(self):
        return [key for key, group in groupby(self.list)]


R1 = RemoveDuplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
R1.rem()
print('original list:')
print(R1.list)
print('After removing consecutive duplicates:')
print(R1.rem())
