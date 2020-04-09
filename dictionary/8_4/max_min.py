# Write a Python program to get the maximum and minimum value in a dictionary
# my_dict = {'x':500, 'y':5874, 'z': 560}
#
# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
#
# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])
class Max_min:
    def __init__(self,dict):
        self.dict = dict

    def mai(self):
        key_max = max(self.dict.keys(), key=(lambda k: self.dict[k]))
        key_min = min(self.dict.keys(), key=(lambda k: self.dict[k]))
        print('maximum ', self.dict[key_max])
        print('minimum ', self.dict[key_min])
M1 = Max_min({'x':500, 'y':5874, 'z': 560})
M1.mai()