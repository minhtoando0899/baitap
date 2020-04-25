"""Bài tập: Viết hàm myfunc tính tổng tất cả
các phần tử có cả hai chỉ số đều chẵn của một ma trận A bất kỳ."""
import numpy as np


class Matrix:
    def __init__(self, A):
        self.A = A

    def sum(self):
        A_1 = np.sum(self.A[[range(0, self.A.shape[0], 2)]][:, range(0, self.A.shape[1], 2)])
        print(A_1)


A = np.array([[1, 2, 3, 4, 2], [5, 6, 7, 8, 3], [9, 10, 11, 12, 4]])
M1 = Matrix(A)
M1.sum()
