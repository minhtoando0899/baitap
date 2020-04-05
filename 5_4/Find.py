# Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# x = [(4, 1), (1, 2), (6, 0)]
# print(min(x, key=lambda n: (n[1], -n[0])))

class Find_smallest_second:
    def __init__(self, list):
        self.list = list

    def fin(self):
        print(min(self.list, key=lambda n: (n[1], -n[0])))


F1 = Find_smallest_second([(4, 1), (1, 2), (6, 0)])
F1.fin()
