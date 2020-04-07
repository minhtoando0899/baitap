# Write a Python program to shuffle and print a specified list.
from random import shuffle
class Shuffle:
    def __init__(self,list):
        self.list = list

    def shu(self):
        shuffle(self.list,None)

S1 = Shuffle(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
S1.shu()
print(S1.list)