# # Write a Python program to split a list every Nth element.
# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# def list_slice(S, step):
#     return [S[i::step] for i in range(step)]
# print(list_slice(C,3))

class Split:
    def __init__(self, list, step):
        self.list = list
        self.step = step

    def spl(self):
        return [self.list[i::self.step] for i in range(self.step)]


S1 = Split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3)
S1.spl()
print(S1.spl())
