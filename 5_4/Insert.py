# Write a Python program to insert a given string at the beginning of all items in a list.
class Insert:
    def __init__(self, list):
        self.list = list

    def ins(self):
        print(['abc{0}'.format(i) for i in self.list])


I1 = Insert([1, 2, 3, 4, 5])
I1.ins()
