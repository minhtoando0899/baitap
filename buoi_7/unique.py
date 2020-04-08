# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Write a Python program to print all unique values in a dictionary.
class Unique:
    def __init__(self, dic):
        self.dic = dic

    def uni(self):
        new_dic = set(val for dic in self.dic for val in dic.values())
        print(new_dic)


U1 = Unique(
    [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}])
U1.uni()
