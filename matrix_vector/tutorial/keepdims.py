"""keepdims = True
Đôi khi, để thuận tiện cho việc tính toán về sau, chúng ta muốn kết quả trả về
khi axis = 0 là các vector hàng thực sự, khi axis = 1 là các vector cột thực sự.
Để làm được việc đó, Numpy cung cấp thuộc tính keepdims = True (mặc định là False).
Khi keepdims = True, nếu sử dụng axis = 0, kết quả sẽ là một mảng hai chiều có
chiều thứ nhất bằng 1 (coi như ma trận một hàng). Tương tự, nếu sử dụng axis = 1,
kết quả sẽ là một mảng hai chiều có chiều thứ hai bằng 1 (một ma trận có số cột bằng 1)."""

import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A)

print("_______________________")

print(np.sum(A, axis=0, keepdims=True))  # Định nghĩa lại axis = 0 là một HÀNG thực sự.

print("_______________________")

print(np.mean(A, axis=1, keepdims=True))  # Định nghĩa lại axis = 1 là một CỘT thực sự.
