# Write a Python program to get the difference between the two lists
class Difference:
    def __init__(self,list_1,list_2):
        self.list_1 = list_1
        self.list_2 = list_2
        self.list_dif = []
    def diff(self):
        self.list_dif = (list(set(self.list_1)-set(self.list_2)))

D1 = Difference([1,2,3,4],[1,2])
D1.diff()
print(D1.list_dif)