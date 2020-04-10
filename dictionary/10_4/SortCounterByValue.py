# Write a Python program to sort Counter by value.
from collections import Counter


class CounterValues:
    def __init__(self, dict):
        self.dict = dict

    def cou(self):
        x = Counter(self.dict)
        print(x.most_common())


C1 = CounterValues({'Math': 81, 'Physics': 83, 'Chemistry': 87})
C1.cou()