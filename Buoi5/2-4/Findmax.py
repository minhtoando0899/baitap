class Findmax:
    def __init__(self, list):
        self.list = list
        self.max_1 = self.list[0]

    def max(self):
        for x in self.list:
            if self.max_1 < x:
                self.max_1 = x


m1 = Findmax([1, 23, 6547, 435, 4234, 5321, 223])
m1.max()
print(m1.max_1)
