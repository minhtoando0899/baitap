'''Write a Python program to generate and print a list of first and last 5 elements
 where the values are square of numbers
between 1 and 30 (both included).'''


class Print:
    def __init__(self, list):
        self.list = list
        self.list_1 = []

    def square(self):
        for x in self.list:
            self.list_1.append(x ** 2)


S1 = Print(list(range(51)))
S1.square()
print(S1.list_1[:5])
print(S1.list_1[-5:])
