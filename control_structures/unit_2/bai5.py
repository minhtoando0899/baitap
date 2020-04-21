while True:
    class Daysofmonth:
        def __init__(self):
            self.thang = int()
            self.nam = int()

        def get(self):
            self.thang = int(input("Nhập tháng: "))
            self.nam = int(input("Nhập năm: "))

        def find(self):
            if self.thang in list([1, 3, 5, 7, 8, 10, 12]):
                print("Tháng %s năm %s có 31 ngày!" % (self.thang, self.nam))
            if self.thang in list([4, 6, 9, 11]):
                print("Tháng %s năm %s có 30 ngày!" % (self.thang, self.nam))
            if self.thang == 2:
                if self.nam % 100 == 0 and self.nam % 400 != 0:
                    print("Tháng %s năm %s có 28 ngày!" % (self.thang, self.nam))
                elif self.nam % 4 == 0:
                    print("Tháng %s năm %s có 29 ngày!" % (self.thang, self.nam))
                else:
                    print("Tháng %s năm %s có 28 ngày!" % (self.thang, self.nam))


    D1 = Daysofmonth()
    D1.get()
    D1.find()
