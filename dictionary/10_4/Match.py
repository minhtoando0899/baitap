# Write a Python program to match key values in two dictionaries.

class Match:
    def __init__(self, dict_1, dict_2):
        self.dict_1 = dict_1
        self.dict_2 = dict_2

    def mat(self):
        for (key, value) in set(self.dict_1.items()) & set(self.dict_2.items()):
            print('%s : %s is present in both dict_1 and dict_2' % (key, value))


M1 = Match({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})
M1.mat()