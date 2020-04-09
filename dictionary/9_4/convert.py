# Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# new_dict = current = {}
# for name in num_list:
#     current[name] = {}
#     current = current[name]
# print(new_dict)
class Convert:
    def __init__(self, list):
        self.list = list

    def con(self):
        new_dict = current = {}
        for name in self.list:
            current[name] = {}
            current = current[name]
        print(new_dict)


C1 = Convert([1, 2, 3, 4])
C1.con()
