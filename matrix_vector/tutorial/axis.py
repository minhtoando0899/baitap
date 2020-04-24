"""axis = 0 là tính theo chiều từ trên xuống dưới,
nghĩa là phương của nó cùng với phương của các cột.
Tương tự axis = 1 sẽ có phương cùng với phương của các hàng."""

import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A)

print("_______________________")

# #####################################################
# np.sum, np.min, np.max, np.mean cho mảng nhiều chiều.
# -----------------------------------------------------

# axis = 0 (tác động lên các cột của A).
print(np.sum(A, axis=0))
print(np.max(A, axis=0))
print(np.min(A, axis=0))
print(np.mean(A, axis=0))  # giá trị trung bình của các cột trong mt A

print("_______________________")

# axis = 1 (tác động lên các hàng của A).
print(np.sum(A, axis=1))
print(np.max(A, axis=1))
print(np.min(A, axis=1))
print(np.mean(A, axis=1))

