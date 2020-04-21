# kiem tra 1 so nguyen co phai la so nguyen to khong
import math

while True:
    class Check:
        def __init__(self):
            self.n = int

        def get(self):
            self.n = int(input("Nhập số nguyên: "))

        def che(self):
            if self.n < 2:
                print("Nhập số lớn hơn 2")
            if self.n >= 2:
                for x in range(2, int(math.sqrt(self.n) + 1)):
                    if self.n % x == 0:
                        print("%s không phải là số nguyên tố!!!" % self.n)
                        break
                else:
                    print("%s là số nguyên tố!!!" % self.n)


    C1 = Check()
    C1.get()
    C1.che()
