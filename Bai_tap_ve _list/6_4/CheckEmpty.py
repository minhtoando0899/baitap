# Write a Python program to check whether all dictionaries in a list are empty or not
# my_list = [{},{},{}]
# my_list1 = [{1,2},{},{}]
# print(all(not d for d in my_list))
# print(all(not d for d in my_list1))
class CheckEmpty:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def che(self):
        print(all(not x for x in self.list_1))
        print(all(not x for x in self.list_2))


C1 = CheckEmpty([{}, {}, {}], [{1, 2}, {}, {}])
C1.che()
