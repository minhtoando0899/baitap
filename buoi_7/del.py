#  Write a Python program to remove a key from a dictionary.
class Delete:
    def __init__(self, dic, key):
        self.key = key
        self.dic = dic

    def dele(self):
        if self.key in self.dic:
            del self.dic[self.key]
            print(self.dic)


D1 = Delete({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'a')
D1.dele()
print(D1.dele())
