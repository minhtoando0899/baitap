# # Write a Python program to flatten a given nested list structure.
# def flatten_list(n_list):
#     result_list = []
#     if not n_list: return result_list
#     stack = [list(n_list)]
#     while stack:
#         c_num = stack.pop()
#         next = c_num.pop()
#         if c_num: stack.append(c_num)
#         if isinstance(next, list):
#             if next: stack.append(list(next))
#         else: result_list.append(next)
#     result_list.reverse()
#     return result_list
# n_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# print("Original list:")
# print(n_list)
# print("\nFlatten list:")
# print(flatten_list(n_list))
class Flatten:
    def __init__(self, list):
        self.list = list

    def fla(self):
        result_list = []
        if not self.list: return result_list
        stack = [list(self.list)]
        while stack:
            c_num = stack.pop()
            next = c_num.pop()
            if c_num: stack.append(c_num)
            if isinstance(next, list):
                if next: stack.append(list(next))
            else:
                result_list.append(next)
        result_list.reverse()
        return result_list


F1 = Flatten([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
F1.fla()
print(F1.fla())
