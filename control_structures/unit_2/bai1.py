class Findmax:
    def __init__(self, list):
        self.list = list
        self.max_1 = self.list[0]

    def fin(self):
        for i in range(len(self.list)):
            if self.max_1 < self.list[i]:
                self.max_1 = self.list[i]
        print(self.max_1)


F1 = Findmax([1, 200, 3])
F1.fin()
