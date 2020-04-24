"""Cho một ma trận A, viết hàm myfunc tính tổng các phần tử
trên các cột có chỉ số chẵn (0, 2, 4, ...) của ma trận đó."""

import numpy as np


class Sum:
    def __init__(self, A):
        self.A = A

    def myfunc(self):
        A_1 = np.sum(self.A[[0, 1]][:, [range(0, self.A.shape[1], 2)]])
        print(A_1)


A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
S = Sum(A)
print(S.A)
S.myfunc()
