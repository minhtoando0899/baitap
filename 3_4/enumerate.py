# Write a Python program access the index of a list.
class Enumerate:
    def __init__(self,list):
        self.list = list

    def enum(self):
        for index,val in enumerate(self.list,start=1):
            print(index,val)

E1 = Enumerate([5, 15, 35, 8, 98])
E1.enum()