'''Write a Python program to generate and print a list except for the first 5 elements,
 where the values are square of numbers between 1 and 30 (both included)'''


class Square:
    def __init__(self, list):
        self.list = list
        self.list_1 = []

    def squa(self):
        for x in self.list:
            self.list_1.append(x ** 2)


S1 = Square(list(range(31)))
S1.squa()
print(S1.list_1[4:])
