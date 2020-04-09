# Write a Python program to get the top three items in a shop.
# from heapq import nlargest
# from operator import itemgetter
# items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for name, value in nlargest(3, items.items(), key=itemgetter(1)):
#     print(name, value)
from heapq import nlargest
from operator import itemgetter


class Get_3_largest:
    def __init__(self, dict):
        self.dict = dict

    def get(self):
        for name, value in nlargest(3, self.dict.items(), key=itemgetter(1)):
            print(name, value)


G1 = Get_3_largest({'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24})
G1.get()
