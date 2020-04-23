# Nhập 1 số bất kỳ kiểm tra xem có nằm ở trong dãy ko, có thì in ra vị trí của số đó.
# import random
# n = random.sample(range(1, 100), 10)
# print(n)
while True:
    class Random:
        def __init__(self):
            self.n = int()
            self.list = [21, 17, 10, 63, 46, 51, 20, 49, 67, 30]

        def get(self):
            self.n = int(input("Nhập số bất kỳ: "))

        def check(self):
            if self.n in self.list:
                print("Số %s nằm ở vị trí %s" % ((self.n), (self.list.index(self.n))))
            else:
                print("%s không nằm trong dãy số, nhập lại!" % self.n)


    R1 = Random()
    R1.get()
    R1.check()
