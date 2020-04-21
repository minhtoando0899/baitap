# in ra màn hình dãy số nguyên dương lẻ nhỏ hơn số N nào đó được nhập từ bàn phím
while True:
    class Integer:
        def __init__(self):
            self.n = int()

        def get(self):
            self.n = int(input("Nhập 1 số: "))

        def fin(self):
            for x in range(0, self.n):
                if x % 2 != 0:
                    print(x)


    I1 = Integer()
    I1.get()
    I1.fin()
