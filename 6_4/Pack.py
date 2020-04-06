# # Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# from itertools import groupby
# def pack_consecutive_duplicates(l_nums):
#     return [list(group) for key, group in groupby(l_nums)]
# n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
# print("Original list:")
# print(n_list)
# print("\nAfter packing consecutive duplicates of the said list elements into sublists:")
# print(pack_consecutive_duplicates(n_list))
from itertools import groupby


class PackDuplicates:
    def __init__(self, list):
        self.list = list

    def pac(self):
        return [list(group) for key, group in groupby(self.list)]


P1 = PackDuplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
P1.pac()
print('original list')
print(P1.list)
print('Apter packing consecutive diplicates of the said list elements into sublists:')
print(P1.pac())
