# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
#
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
#
# print(dup_items)

class Delete:
    def __init__(self, list):
        self.list = list
        self.set_1 = {}

    def Set(self):
        for x in self.list:
            if x not in self.set_1:
                set.add(self.set_1,x)

