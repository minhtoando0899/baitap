import numpy as np

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]
A_1 = np.array(A)
B_1 = np.array(B)
print('A+B: ', A_1 + B_1)  # Plus
print('_________________________')
print('A-B: ', A_1 - B_1)  # Minus
print('_________________________')
print('A*B: ', A_1 * B_1)  # Multiply
print('_________________________')
print('A/B: ', A_1 / B_1)  # Division
