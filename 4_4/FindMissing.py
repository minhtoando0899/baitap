# # Write a Python program to find missing and additional values in two lists.
# list1 = ['a','b','c','d','e','f']
# list2 = ['d','e','f','g','h']
# print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
# print('Additional values in second list: ', ','.join(set(list2).difference(list1)))

class Find_Missing:
    def __init__(self,list_1,list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def fin(self):
        print('missing values in second list: ', ','.join(set(self.list_1).difference(self.list_2)))
        print('additional values in second list:', ','.join(set(self.list_2).difference(self.list_1)))

F1 = Find_Missing(['a','b','c','d','e','f'],['d','e','f','g','h'])
F1.fin()