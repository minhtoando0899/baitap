# Write a Python program to flatten a shallow list.
import itertools
class Flattend:
    def __init__(self,list):
        self.list_1 = list
        self.list_2 = []

    def flat(self):
        self.list_2 = list(itertools.chain(*self.list_1))

F1 = Flattend([[2,4,3],[1,5,6], [9], [7,9,0]])
F1.flat()
print(F1.list_2)