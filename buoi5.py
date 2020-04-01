class PhepNhan:
    def __init__(self, list):
        self.list_1 = list
        self.sum_1 = 0

    def sum(self):
        for x in self.list_1:
            self.sum_1 += x


s1 = PhepNhan([1, 2, 3, 4, 5])
s1.sum()
print(s1.sum_1)


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

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
