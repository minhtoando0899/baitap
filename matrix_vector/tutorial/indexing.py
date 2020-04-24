import numpy as np

A = [[1, 2, 3], [4, 5, 6]]
A_1 = np.array(A)
print(A_1)
print('A_1[0,2]: ', A_1[0, 2])  # get element three of row 1
print('A_1[1,2]: ', A_1[1, 2])  # get element three of row 2
print('A_1[:,2]: ', A_1[:, 2])  # get all element of column 3
print('A_1[1,:]: ', A_1[1, :])  # get all element of row 2
print("-------------------------------")

# Truy cập nhiều phần tử.
A_1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(A_1)
print(A)
print("-------------------------------")

# Nhiều phần tử trong 1 hàng.
print(A[0, 2:])
print(A[1, range(0, A.shape[1], 2)])  # In ra các phần tử từ 0 đến cột cuối của A với bước nhảy là 2.
print("-------------------------------")

# Nhiều phần tử trong cùng 1 cột.
print(A[[0, 1, 2], 0])  # In ra các phần tử vị trí 0 ở hàng 1, 2, 3.
print("-------------------------------")

# Nhiều hàng nhiều cột.
print(A[[1, 2]][:, [0, 1]])  # In ra các phần tử ở vị trí 0, 1 ở hàng 1 và 2.
print("-------------------------------")

# Cặp tọa độ.
print(A[[1, 2], [1, 3]])  # In ra tọa độ hàng 1, 2 vị trí 1 và 3.
print(A[[1, 2], [1]])  # In ra tọa độ hàng 1, 2 ở tất cả các vị trí 1.
