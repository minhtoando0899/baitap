# Write a Python program to clone or copy a list.
class Copy:
    def __init__(self,list):
        self.list = list
        self.list_1 = []
    def clone(self):
        self.list_1=list(self.list)

C1 = Copy([1,2,343,263,6])
C1.clone()
print(C1.list_1)