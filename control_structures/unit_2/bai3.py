class NamNhuan:
    def __init__(self, nam):
        self.nam = nam

    def fin(self):
        if self.nam % 100 == 0 and self.nam % 400 != 0:
            print("%s không phải là năm nhuận!" % self.nam)
        elif self.nam % 4 == 0:
            print("%s là năm nhuận!" % self.nam)
        else:
            print("%s không phải là năm nhuận!")


N1 = NamNhuan(1700)
N1.fin()
