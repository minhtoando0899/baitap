# # Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
#
# import itertools
# d ={'1':['a','b'], '2':['c','d']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))
import itertools


class Combinations:
    def __init__(self, dic):
        self.dic = dic

    def com(self):
        for comb in itertools.product(*[self.dic[k] for k in sorted(self.dic.keys())]):
            print(''.join(comb))


C1 = Combinations({'1': ['a', 'b'], '2': ['c', 'd']})
C1.com()
