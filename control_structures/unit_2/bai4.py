import math


class Giaipt:
    def __init__(self):
        self.a = float()
        self.b = float()
        self.c = float()

    def get(self):
        self.a = float(input("Nhập hệ số bậc 2: "))
        self.b = float(input("Nhập hệ số bậc 1: "))
        self.c = float(input("Nhập hệ số tự do: "))

    def ngh(self):
        self.delta = (self.b ** 2) - (4 * self.a * self.c)
        if self.delta == 0:
            x = -self.b / (2 * self.a)
            print("Phương trình có nghiệm kép là: ", x)

        elif self.delta > 0:
            x1 = float((-self.b - math.sqrt(self.delta)) / (2 * self.a))
            x2 = float((-self.b + math.sqrt(self.delta)) / (2 * self.a))
            print("Phương trình có 2 nghiệm là: ", "x1 = ", x1, " và ", "x2 = ", x2)

        else:
            print("Phương trình vô nghiệm!")


G1 = Giaipt()
G1.get()
G1.ngh()
