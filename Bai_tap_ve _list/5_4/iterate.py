# # Write a Python program to iterate over two lists simultaneously.
# num = [1, 2, 3]
# color = ['red', 'white', 'black']
# for (a,b) in zip(num, color):
#      print(a, b)

class Iterate:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def ite(self):
        for (a, b) in zip(self.list_1, self.list_2):
            print(a, b)


I1 = Iterate([1, 2, 3], ['res', 'white', 'black'])
I1.ite()
