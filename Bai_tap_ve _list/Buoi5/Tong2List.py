class HHH:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.tong1 = 0

    def Tong(self):
        for a in self.list1:
            self.tong1 += a

    def Append(self):
        list.append(self.list2, self.tong1)

    def Tong2(self):
        for b in self.list2:
            self.tong1 += b


h1 = HHH([1, 2, 3], [4, 5, 6])
h1.Tong()
h1.Tong2()
print(h1.tong1)
