"""Bài tập: Frobenious norm

Frobenius norm của một ma trận được định nghĩa là căn bậc hai
của tổng bình phương các phần tử của ma trận. Frobenius norm
được sử dụng rất nhiều trong các thuật toán Machine Learning
vì các tính chất toán học đẹp của nó, trong đó quan trọng
nhất là việc đạo hàm của bình phương của nó rất đơn giản.
Frobenius norm của một ma trận
A được ký hiệu là ||A||F"""
import numpy as np
import math

A = np.array([[1, 2, 3], [4, 5, 6]])


def myfunc(A):
    b = sum(list(sum(A ** 2)))
    print(math.sqrt(b))


myfunc(A)
