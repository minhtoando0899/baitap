"""
Bài tập: Hãy tạo ma trận A sau một cách nhanh nhất, không dùng cách thủ công ghi từng phần tử ra.

[[1, 5, 9, 2]
 [6, 10, 3, 7]
 [11, 4, 8, 12]]

Gợi ý:
sử dụng np.arange()
Để ý vị trí của 9, 10, 11 và 2, 3, 4
Lời giải không quá hai dòng
Bạn có thể nhận được phản hồi ‘Kết quả thành công’ nhưng
hãy thử cố nghĩ quy luật của ma trận này rồi dùng các phép transpose, reshape thích hợp.

"""
import numpy as np

print(np.transpose((np.arange(1, 13).reshape(3, -1)).reshape(4, -1, order="F")))
