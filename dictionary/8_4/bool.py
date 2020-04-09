# Write a Python program to check a dictionary is empty or not.
class Bool:
    def __init__(self, dic):
        self.dic = dic

    def boo(self):
        if not bool(self.dic):
            print('the dictionary is empty')


B1 = Bool({})
B1.boo()
