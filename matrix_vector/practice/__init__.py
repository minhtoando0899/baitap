import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A.shape)
print(np.sum(A[[range(0, A.shape[0], 2)]][:, range(0, A.shape[1], 2)]))
