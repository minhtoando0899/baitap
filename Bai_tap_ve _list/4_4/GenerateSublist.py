# Write a Python program to generate all sublists of a list.
# from itertools import combinations
# def sub_lists(my_list):
# 	subs = []
# 	for i in range(0, len(my_list)+1):
# 	  temp = [list(x) for x in combinations(my_list, i)]
# 	  if len(temp)>0:
# 	    subs.extend(temp)
# 	return subs
from itertools import combinations


class Sublist:
    def __init__(self, list):
        self.list = list
        self.subs = []

    def sub(self):
        for i in range(0, len(self.list) + 1):
            temp = [list(x) for x in combinations(self.list, i)]
            if len(temp) > 0:
                self.subs.append(temp)
        return self.subs


S1 = Sublist([10, 20, 30, 40])
S1.sub()
print(S1.sub())
