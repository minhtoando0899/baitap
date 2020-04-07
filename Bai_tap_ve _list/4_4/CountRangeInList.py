#  Write a Python program to count the number of elements in a list within a specified range.
# def count_range_in_list(li, min, max):
# 	ctr = 0
# 	for x in li:
# 		if min <= x <= max:
# 			ctr += 1
# 	return ctr
#
# list1 = [10,20,30,40,40,40,70,80,99]
# print(count_range_in_list(list1, 40, 100))
#
# list2 = ['a','b','c','d','e','f']
# print(count_range_in_list(list2, 'a', 'e'))

class Count_Range_List:
    def __init__(self, list, min, max):
        self.list = list
        self.min = min
        self.max = max
        self.ctr = 0

    def coun(self):
        for x in self.list:
            if self.min <= x <= self.max:
                self.ctr += 1
        return self.ctr


C1 = Count_Range_List([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100)
C1.coun()
print(C1.ctr)
