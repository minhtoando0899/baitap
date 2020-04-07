'''Write a Python program to get a list,
sorted in increasing order by the last element
in each tuple from a given list of non-empty tuples.
'''

# def last(n): return n[-1]
#
# def sort_list_last(tuples):
#   return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
from operator import itemgetter


class Sort:
    def __init__(self, list):
        self.list = list

    def sort_last(self):
        return sorted(self.list, key=itemgetter(-1))


S1 = Sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
S1.sort_last()
print(S1.sort_last())