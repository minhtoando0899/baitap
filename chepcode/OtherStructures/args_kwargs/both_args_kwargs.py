class AragsKwargs:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def myfunc(self):
        print("args:", self.args)
        print("kwargs", self.kwargs)


AK1 = AragsKwargs('DO', 'MINH', 'TOAN', ho='Do', tendem='MINH', ten='TOAN')
AK1.myfunc()