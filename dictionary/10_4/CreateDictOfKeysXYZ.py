# Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Access the fifth value of each key from the dictionary.
from pprint import pprint


class CreateDictOfKeysXYZ:
    def __init__(self, dict):
        self.dict = dict

    def cre(self):
        pprint(self.dict)
        print(self.dict['x'][4])
        print(self.dict['y'][4])
        print(self.dict['z'][4])
        for k, v in self.dict.items():
            print(k, 'has value', v)


C1 = CreateDictOfKeysXYZ(dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40))))
C1.cre()
