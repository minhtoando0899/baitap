""" Với một số tự nhiên n, hãy viết hàm trả về ma trận có dạng:
đường chéo phụ ngay dưới đường chéo chính nhận các giá trị từ 1 đến n.
Các thành phần là kiểu số nguyên."""
import numpy as np

while True:
    class DuongCheo:
        def __init__(self):
            self.n = int()
            self.list = []

        def get(self):
            self.n = int(input("Nhap so n: "))

        def pri(self):
            for i in range(1, self.n + 1):
                self.list.append(i)
            print(np.diag(list(self.list), k=-1))


    D1 = DuongCheo()
    D1.get()
    D1.pri()
