# Write a Python program to print the numbers of a specified list after removing even numbers from it

class Num:
    def __init__(self, list):
        self.list = list
        self.list_1 = []

    def remo(self):
        for x in self.list:
            if x % 2 != 0:
               self.list_1.append(x)
R1 = Num(list(range(101)))
R1.remo()
print(R1.list_1)
