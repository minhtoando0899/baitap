# # Write a Python program to print a nested lists (each list on a new line) using the print() function.
# colors = [['Red'], ['Green'], ['Black']]
# print('\n'.join([str(lst) for lst in colors]))
class Print_A_nested_lists:
    def __init__(self,list):
        self.list = list
        self.list_1 = []

    def pri(self):
        print('\n'.join([str(self.list_1)for self.list_1 in self.list]))
P1 = Print_A_nested_lists([['Red'], ['Green'], ['Black']])
P1.pri()
