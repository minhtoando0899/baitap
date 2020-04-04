# Tìm các số chẵn và các số cấu tạo lên số ấy cũng là số chẵn.
# c = []
# for x in range(1,500):
#     b = list(str(x))
#     dem = 0
#     for i in b:
#         if int(i) % 2 == 0:
#             dem +=1
#         if dem == len(b):
#             c.append(x)
# print(c)
class Count_number:
    def __init__(self, list):
        self.list = list
        self.list_1 = []

    def count(self):
        for x in self.list:
            a = list(str(x))
            dem = 0
            for y in a:
                if int(y) % 2 == 0:
                    dem += 1
                if dem == len(a):
                    self.list_1.append(x)


C1 = Count_number(list(range(501)))
C1.count()
print(C1.list_1)
