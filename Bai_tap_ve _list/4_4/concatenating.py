# # Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# my_list = ['p', 'q']
# n = 4
# new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
# print(new_list)
class Concatenating:
    def __init__(self, list):
        self.list = list
        self.list_new = []

    def conc(self):
        n = 4
        self.list_new = ['{}{}'.format(x, y) for x in self.list for y in range(1, n + 1)]


C1 = Concatenating(['p', 'q'])
C1.conc()
print(C1.list_new)
