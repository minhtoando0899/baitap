# Write a Python program to create a dictionary from a string.
# from collections import defaultdict, Counter
# str1 = 'w3resource'
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)
from collections import defaultdict, Counter


class Create:
    def __init__(self, str1):
        self.str1 = str1
        self.my_dict = {}

    def cre(self):
        for x in self.str1:
            self.my_dict[x] = self.my_dict.get(x, 0) + 1
        print(self.my_dict)

C1 = Create('w3resource')
C1.cre()
