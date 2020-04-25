"""
Bài tập: Cho một ma trận A bất kỳ. Trong mỗi hàng, ta định nghĩa
độ biến động của nó là sự khác nhau giữa giá trị lớn nhất và nhỏ nhất
của các phần tử trong hàng đó. Hãy viết hàm myfunc trả về tổng độ biến động
của tất cả các hàng trong ma trận đó.
"""

import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


def myfunc(self):
    A_1 = (np.max(self, axis=1, keepdims=True) - np.min(self, axis=1, keepdims=True))
    print(np.sum(A_1))


myfunc(A)
