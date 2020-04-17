import numpy as np

A = [[1, 2, 3], [4, 5, 6]]
A_1 = np.array(A)
print('A_1[0,2]: ', A_1[0, 2])  # get element three of row 1
print('A_1[0,1]: ', A_1[1, 2])  # get element three of row 2
print('A_1[:,2]: ', A_1[:, 2])  # get all element of column 3
print('A_1[1,:]: ', A_1[1, :])  # get all element of row 2

