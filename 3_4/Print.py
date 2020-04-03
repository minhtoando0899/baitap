# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)
class Print:
    def __init__(self, list):
        self.list = list
        self.list_1 = []

    def pri(self):
        self.list_1 = [x for (i, x) in enumerate(self.list) if i not in (0, 4, 5)]


P1 = Print(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
P1.pri()
print(P1.list_1)
