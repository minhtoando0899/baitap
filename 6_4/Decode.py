# # Write a Python program to decode a run-length encoded given list
# def decode(alist):
#     def aux(g):
#         if isinstance(g, list):
#             return [(g[1], range(g[0]))]
#         else:
#             return [(g, [0])]
#     return [x for g in alist for x, R in aux(g) for i in R]
# n_list = [[2, 1], 2, 3, [2, 4], 5, 1]
# print("Original encoded list:")
# print(n_list)
# print("\nDecode a run-length encoded said list:")
# print(decode(n_list))

class Decode:
    def __init__(self, list):
        self.list = list

    def dec(self):
        def aux(g):
            if isinstance(g, list):
                return [(g[1], range(g[0]))]
            else:
                return [(g, [0])]

        return [x for g in self.list for x, R in aux(g) for i in R]


D1 = Decode([[2, 1], 2, 3, [2, 4], 5, 1])
D1.dec()
print("Original encoded list:")
print(D1.list)
print("Decode a run-length encoded said list:")
print(D1.dec())
