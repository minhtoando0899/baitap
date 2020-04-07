# Write a Python program to find the index of an item in a specified list.
# num =[10, 30, 4, -6]
# print(num.index(30))
class Index:
    def __init__(self,list):
        self.list_1 = list
        self.list_2 = []
    def ind(self):
        self.list_2 = list(self.list_1)
        print(self.list_2.index(30,0,3))

I1 = Index([10,30,4,-6])
I1.ind()