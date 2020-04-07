# Write a Python program to append a list to the second list.
class Append:
    def __init__(self,list_1,list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def app(self):
        x = self.list_1 + self.list_2
        print(x)

A1 = Append([1, 2, 3, 0],['Red', 'Green', 'Black'])
A1.app()
