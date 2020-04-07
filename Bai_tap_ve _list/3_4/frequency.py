# Write a Python program to get the frequency of the elements in a list.
import collections
class Frequency:
    def __init__(self, list):
        self.list = list

    def fre(self):
        ctr = collections.Counter(self.list)
        print(ctr)

F1 = Frequency([10,10,10,10,20,20,20,20,40,40,50,50,30])
F1.fre()