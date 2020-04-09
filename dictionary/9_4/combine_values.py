# # Write a Python program to combine values in python list of dictionaries.
#
# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(result)
from collections import Counter


class Combine_values:
    def __init__(self, dict):
        self.dict = dict
        self.result = Counter()

    def com(self):
        for d in self.dict:
            self.result[d['item']] += d['amount']
        print(self.result)


C1 = Combine_values(
    [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}])
C1.com()
