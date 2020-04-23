# in ra tất cả số chính phương nhỏ hơn số N
import math

while True:
    class Scp:
        def __init__(self):
            self.n = int

        def get(self):
            self.n = int(input("Nhập số điều kiện: "))

        def fin(self):
            for x in range(1, self.n):
                if math.sqrt(x) == int(math.sqrt(x)):
                    print(x)


    S1 = Scp()
    S1.get()
    S1.fin()
