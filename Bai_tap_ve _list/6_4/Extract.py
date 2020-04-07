# Write a Python program to extract a given number of randomly selected elements from a given list.
# import random
# def random_select_nums(n_list, n):
#         return random.sample(n_list, n)
# n_list = [1,1,2,3,4,4,5,1]
# print("Original list:")
# print(n_list)
# selec_nums = 3
# result = random_select_nums(n_list, selec_nums)
# print("\nSelected 3 random numbers of the above list:")
# print(result)
import random


class Extract:
    def __init__(self, list, n):
        self.list = list
        self.n = n

    def ext(self):
        return random.sample(self.list, self.n)


E1 = Extract([1, 1, 2, 3, 4, 4, 5, 1], 5)
print("Original list:")
print(E1.list)
print("Selected 3 random numbers of the above list:")
print(E1.ext())
