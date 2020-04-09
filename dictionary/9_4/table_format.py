# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)
class Table_format:
    def __init__(self, dict):
        self.dict = dict

    def tab(self):
        for row in zip(*([key] + (value) for key, value in sorted(self.dict.items()))):
            print(*row)


T1 = Table_format({'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]})
T1.tab()
