# # Write a Python program to remove duplicates from a list of lists.
# import itertools
# num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# print("Original List", num)
# num.sort()
# new_num = list(num for num,_ in itertools.groupby(num))
# print("New List", new_num)

import itertools


class Remove:
    def __init__(self, list):
        self.list = list

    def rem(self):
        print(self.list)
        self.list.sort()
        new_list = list(self.list for self.list,_ in itertools.groupby(self.list))
        print(new_list)


R1 = Remove([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])
R1.rem()
