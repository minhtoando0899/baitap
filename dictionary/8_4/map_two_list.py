# Write a Python program to map two lists into a dictionary.
class Map2lists:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.dict = dict

    def map(self):
        D = self.dict(zip(self.key, self.value))
        print(D)


M1 = Map2lists(['red', 'green', 'blue'], ['#FF0000', '#008000', '#0000FF'])
M1.map()
