# Write a Python program to concatenate elements of a list
class Concatenate:
    def __init__(self, list):
        self.list = list

    def con(self):
        print('*'.join(self.list))
        print('~'.join(self.list))


C1 = Concatenate(['anh', 'yeu', 'em'])
C1.con()
