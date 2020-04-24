# Ma trận đường chéo dùng hàm diag().
import numpy as np

# Khai báo 1 ma trận đường chéo.
A_1 = np.diag([1, 2, 3])
print(A_1)
print("-_-_-_-_-_-_-_-_-_-")

# trích xuất 1 đường chéo trong ma trận.
print(np.diag(A_1, k=0))