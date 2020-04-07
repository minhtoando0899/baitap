# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
class Findhighest:
    def __init__(self, list):
        self.list = list

    def fin(self):
        print(max(self.list, key=sum))


F1 = Findhighest([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]])
F1.fin()
