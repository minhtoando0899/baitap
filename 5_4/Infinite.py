# Write a Python program to create a list with infinite elements.
import itertools


class Infinite:
    def __init__(self, a):
        self.a = a

    def inf(self):
        self.a = itertools.count(0, 1000)
        print(next(self.a))
        print(next(self.a))
        print(next(self.a))
        print(next(self.a))


I1 = Infinite(1)
I1.inf()
