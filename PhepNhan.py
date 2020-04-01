class PhepNhan:
    def __init__(self, list):
        self.list_2 = list
        self.nhan_1 = 1

    def Nhan(self):
        for x in self.list_2:
            self.nhan_1 *= x


s2 = PhepNhan([1, 3, 5, 7, 9])
s2.Nhan()
print(s2.nhan_1)
