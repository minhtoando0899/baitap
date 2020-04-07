# # Write a Python program to compute the similarity between two lists.
# from collections import Counter
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# counter1 = Counter(color1)
# counter2 = Counter(color2)
# print("Color1-Color2: ",list(counter1 - counter2))
# print("Color2-Color1: ",list(counter2 - counter1))
from collections import Counter


class Similarity:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def sim(self):
        counter_1 = Counter(self.list_1)
        counter_2 = Counter(self.list_2)
        print("list_1 - list_2: ", list(counter_1 - counter_2))
        print("list_2 - list_1: ", list(counter_2 - counter_1))


S1 = Similarity(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"])
S1.sim()
