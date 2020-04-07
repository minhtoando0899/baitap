# Write a Python program to replace the last element in a list with another list.
class Replace:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def rep(self):
        self.list_1[-1:] = self.list_2


R1 = Replace([1, 2, 3, 4, 5, 7], [6, 7, 8, 9, 10])
R1.rep()
print(R1.list_1)
