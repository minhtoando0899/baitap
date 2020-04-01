class core:
    def __init__(self, list, tuple, set):
        self.list = list
        self.tuple = tuple
        self.set = set

    def append(self):
        list.append(self.list, 6)
        print(self.list)

    def appendt(self):
        a = list(self.tuple)
        list.append(a, 9)
        self.tuple = a
        print(self.tuple)

    def appends(self):
        set.add(self.set, 12)
        print(self.set)


l1 = core([1, 2, 3, 4, 5], (6, 7, 8), {9, 10, 11})
l1.append()
l1.appendt()
l1.appends()
