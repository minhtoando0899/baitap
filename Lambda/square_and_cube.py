# Write a Python program to square and cube every number in a given list of integers using Lambda.
class Sc:
    def __init__(self, list):
        self.list = list

    def squ(self):
        square = list(filter(lambda x: x ** 2, self.list))
        print(square)

    def cub(self):
        cube = list(map(lambda x: x ** 3, self.list))
        print(cube)


S1 = Sc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
S1.squ()
S1.cub()
