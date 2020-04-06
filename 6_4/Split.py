# # Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# def split_two_parts(n_list, L):
#     return n_list[:L], n_list[L:]
# n_list = [1,1,2,3,4,4,5, 1]
# print("Original list:")
# print(n_list)
# first_list_length = 3
# print("\nLength of the first part of the list:",first_list_length)
# print("\nSplited the said list into two parts:")
# print(split_two_parts(n_list, first_list_length))
class SplitList:
    def __init__(self,list, L):
        self.list = list
        self.L = L

    def spl(self):
        return  self.list[:self.L], self.list[self.L:]

S1 = SplitList([1,1,2,3,4,4,5, 1],3)
S1.spl()
print("Original list:")
print(S1.list)
first_list_length = 3
print("Length of the first part of the list:",first_list_length)
print("Splited the said list into two parts:")
print(S1.spl())