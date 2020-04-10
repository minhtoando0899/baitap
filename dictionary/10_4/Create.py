# Write a Python program to create a dictionary from two lists without losing duplicate values.
# from collections import defaultdict
# class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# id_list = [1, 2, 2, 3]
# temp = defaultdict(set)
# for c, i in zip(class_list, id_list):
#     temp[c].add(i)
# print(temp)
from collections import defaultdict


class CreateDictionary:
    def __init__(self, class_list, id_list):
        self.class_list = class_list
        self.id_list = id_list
        self.temp = defaultdict(set)

    def cre(self):
        for c, i in zip(self.class_list, self.id_list):
            self.temp[c].add(i)
        print(self.temp)


C1 = CreateDictionary(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3])
C1.cre()
