# Write a Python function that takes two lists and returns True if they have at least one common member
class Common:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def com(self):
        for x in self.list_1:
            for y in self.list_2:
                if x == y:
                    return 'True'



C1 = Common([1, 2, 34, 45, 65, 76], [2, 4, 14, 5, 52, 31, 15, 143])
C1.com()
print(C1.com())