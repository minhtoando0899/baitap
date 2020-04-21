from math import sqrt


class Findmin:
    def __init__(self, list_1, list_2, list_3):
        self.list_1 = list_1
        self.list_2 = list_2
        self.list_3 = list_3

    def fin(self):
        a = sqrt((self.list_1[0]) ** 2 + (self.list_1[1]) ** 2 + (self.list_1[2]) ** 2)
        b = sqrt((self.list_2[0]) ** 2 + (self.list_2[1]) ** 2 + (self.list_3[2]) ** 2)
        c = sqrt((self.list_3[0]) ** 2 + (self.list_3[1]) ** 2 + (self.list_3[2]) ** 2)
        d = [a, b, c]
        if a == min(d):
            print(self.list_1)

        elif b == min(d):
            print(self.list_2)

        elif c == min(d):
            print(self.list_3)


F1 = Findmin([10, 60, 30], [46, 50, 56], [70, 81, 9])
print("nearest coordinates is:")
F1.fin()
