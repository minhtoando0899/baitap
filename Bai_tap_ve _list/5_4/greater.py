# Write a Python program to find all the values in a list are greater than a specified number.
class Greater:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def gre(self):
        print(all(x >= 200 for x in self.list_1))
        print(all(x >= 25 for x in self.list_2))


G1 = Greater([300, 200, 400], [1, 2, 3])
G1.gre()
