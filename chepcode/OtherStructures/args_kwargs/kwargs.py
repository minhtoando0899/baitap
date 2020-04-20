class Kwargs:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def myfun(self):
        for key, value in self.kwargs.items():
            print("%s: %s" % (key, value))


K1 = Kwargs(ten='TOAN', tendem='MINH', ho='DO')
K1.myfun()
