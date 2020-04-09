class Check:
    def __init__(self, value):
        self.value = value
        self.Thong_tin = {
            'name': 'Toàn',
            'tuoi': '21',
            'truong': 'Ptit'
        }

    def che(self):
        if self.value in self.Thong_tin.values():
            print('yes')
        else:
            print('no')


C1 = Check('Ptit')
C1.che()
