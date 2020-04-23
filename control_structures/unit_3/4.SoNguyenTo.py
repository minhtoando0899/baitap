# Tính trung bình cộng các số nguyên tố trong khoảng 1 chiều các số nguyên.
import math


class Tbc:
    def __init__(self, list):
        self.list = list
        self.l = []

    def fin(self):
        for x in self.list:
            for i in range(2, int(math.sqrt(x)+1)):
                if x % i == 0:
                    break
            else:
                self.l.append(x)
        print(sum(self.l) / len(self.l))


T1 = Tbc(list(range(1, 50)))
T1.fin()
print(T1.l)
