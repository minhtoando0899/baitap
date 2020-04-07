class abc:
    def __init__(self, set):
        self.set = set

    def union(self):
        b = {4, 5, 6}
        set.update(self.set,b)
        print(self.set)

    def remove(self):
        set.remove(self.set, 2)
        print(self.set)


s1 = abc({1, 2, 3})
s1.union()
s1.remove()
