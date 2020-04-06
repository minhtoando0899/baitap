'''Write a Python program to create a list reflecting
the modified run-length encoding from a given list of integers
or a given list of characters'''
from itertools import groupby
# def modified_encode(alist):
#         def ctr_ele(el):
#             if len(el)>1: return [len(el), el[0]]
#             else: return el[0]
#         return [ctr_ele(list(group)) for key, group in groupby(alist)]
#
# n_list = [1,1,2,3,4,4,5, 1]
# print("Original list:")
# print(n_list)
# print("\nList reflecting the modified run-length encoding from the said list:")
# print(modified_encode(n_list))
#
# n_list = 'aabcddddadnss'
# print("\nOriginal String:")
# print(n_list)
# print("\nList reflecting the modified run-length encoding from the said string:")
# print(modified_encode(n_list))
from itertools import groupby


class ReflectingTheModifed:
    def __init__(self, list):
        self.list = list

    def ref(self):
        def ctr_ele(el):
            if len(el) > 1:
                return [len(el), el[0]]
            else:
                return el[0]

        return [ctr_ele(list(group)) for key, group in groupby(self.list)]


R1 = ReflectingTheModifed([1, 1, 2, 3, 4, 4, 5, 1])
R1.ref()
print('original list:')
print(R1.list)
print('List reflecting the run-length encoding from the said string:')
print(R1.ref())
R2 = ReflectingTheModifed('aabcddddadnss')
R2.ref()
print('original list:')
print(R2.list)
print('List reflecting the run-length encoding from the said string:')
print(R2.ref())