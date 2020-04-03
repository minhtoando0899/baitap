# Write a Python program to select an item randomly from a list.
from random import choice
class Ramdom:
    def __init__(self,list):
        self.list = list

    def ran(self):
        print(random.choice(self.list))

R1 = Ramdom(['Red', 'Blue', 'Green', 'White', 'Black'])
R1.ran()