# Write a Python program to generate all permutations of a list in Python.
from itertools import permutations
class Shuffle:
    def __init__(self,list):
        self.list = permutations(list,None)
        self.list_1 = []

    def permutation(self):
        for x in self.list:
            self.list_1.append(x)

P1 = Shuffle([1,2,3,4,5])
P1.permutation()
print(P1.list_1)