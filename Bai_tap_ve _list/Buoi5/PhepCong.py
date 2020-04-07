class PhepCong:
    def __init__(self, list):
        self.list_1 = list
        self.sum_1 = 0

    def sum(self):
        for x in self.list_1:
            self.sum_1 += x


s1 = PhepCong([1, 2, 3, 4, 5])
s1.sum()
print(s1.sum_1)
