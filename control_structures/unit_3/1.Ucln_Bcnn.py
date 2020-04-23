# Tìm USCLN và BCNN của hai số a, b bất kỳ
while True:
    class Ucln:
        def __init__(self):
            self.a = int()
            self.b = int()
            self.list_a = []
            self.list_b = []

        def get(self):
            self.a = int(input("Nhap so a = "))
            self.b = int(input("Nhap so b = "))

        def fin_ucln(self):
            for x in range(1, self.a + 1):
                if self.a % x == 0:
                    self.list_a.append(x)
            for y in range(1, self.b + 1):
                if self.b % y == 0:
                    self.list_b.append(y)
            list_ab = (set(self.list_a) & set(self.list_b))
            print("USCLN và BCNN của 2 số trên lần lượt là: %s, %s" % (
                max(list_ab), int((self.a * self.b) / max(list_ab))))


    U1 = Ucln()
    U1.get()
    U1.fin_ucln()
