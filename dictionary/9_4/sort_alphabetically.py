# Write a Python program to sort a list alphabetically in a dictionary.
class Sort_alphabetically:
    def __init__(self, dict):
        self.dict = dict

    def sor(self):
        new_dict = {x: sorted(y) for x, y in self.dict.items()}
        print(new_dict)


S1 = Sort_alphabetically({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]})
S1.sor()
