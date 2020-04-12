# 5. Write a Python program to filter a list of integers using Lambda.
class Filter:
    def __init__(self, list):
        self.list = list

    def fil1(self):
        new_1 = list(filter(lambda x: x % 2 == 0, self.list))
        print(new_1)

    def fil2(self):
        new_2 = list(filter(lambda x: x % 2 != 0, self.list))
        print(new_2)


F1 = Filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(F1.list)
F1.fil1()
F1.fil2()
