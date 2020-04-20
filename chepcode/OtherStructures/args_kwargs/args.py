class Args:
    def __init__(self,*args):
        self.args= args

    def myfunc(self):
        for x in self.args:
            print(x)

A1 = Args("DO", "MINH" , "TOAN")
A1.myfunc()