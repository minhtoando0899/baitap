# # Write a Python program to check whether a list contains a sublist.
# def is_Sublist(l, s):
#     sub_set = False
#     if s == []:
#         sub_set = True
#     elif s == l:
#         sub_set = True
#     elif len(s) > len(l):
#         sub_set = False
#
#     else:
#         for i in range(len(l)):
#             if l[i] == s[0]:
#                 n = 1
#                 while (n < len(s)) and (l[i + n] == s[n]):
#                     n += 1
#
#                 if n == len(s):
#                     sub_set = True
#
#     return sub_set
#
#
# a = [2, 4, 3, 5, 7]
# b = [4, 3]
# c = [3, 7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
class Sublist:
    def __init__(self, list, sublist):
        self.list = list
        self.sublist = sublist

    def sub(self):
        sub_set = False
        if self.sublist == []:
            sub_set = True
        elif self.sublist == self.list:
            sub_set = True
        elif len(self.sublist) > len(self.list):
            sub_set = False
        else:
            for i in range(len(self.list)):
                if self.list[i] == self.sublist[0]:
                    n = 1
                    while (n < len(self.sublist)) and (self.list[i + n] == self.sublist[n]):
                        n += 1
                    if n == len(self.sublist):
                        sub_set = True
        return sub_set


S1 = Sublist([2, 4, 3, 5, 7], [4, 3])
S1.sub()
print(S1.sub())
