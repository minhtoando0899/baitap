# # Write a Python program to get the depth of a dictionary.
# def dict_depth(d):
#     if isinstance(d, dict):
#         return 1 + (max(map(dict_depth, d.values())) if d else 0)
#     return 0
# dic = {'a': 1, 'b': {'c': {'d': {}}}}
# print(dict_depth(dic))


class Depth:
    def __init__(self, d):
        self.d = d

    def dep(self):
        if isinstance(self.d, dict):
            return 1 + (max(map(Depth.dep, self.d.values())) if self.d else 0)
        return 0


D1 = Depth({'a': 1, 'b': {'c': {'d': {}}}})
D1.dep()
print(D1.dep())
