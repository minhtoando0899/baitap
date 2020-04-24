import numpy as np

A_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = np.array(A_1)
print("A:\n", A)
print("Tổng các hàng của A: ", np.sum(A, 0))
print("Hàng lớn nhất của A: ", np.max(A, 0))
print("Hàng nhỏ nhất của A: ", np.min(A, 0))
