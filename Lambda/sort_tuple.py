# 3. Write a Python program to sort a list of tuples using Lambda.
class Sort:
    def __init__(self,list):
        self.list = list

    def sor(self):
        self.list.sort(key = lambda x: x[1])

S1 = Sort([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
S1.sor()
print(S1.list)
