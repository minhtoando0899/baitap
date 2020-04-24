# nhân ma trận với ma trận
import numpy

a_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b_1 = [[1, 2], [3, 4], [5, 6]]
a = numpy.array(a_1)
b = numpy.array(b_1)
print("a =\n", a)
print("b =\n", b)
print("a*b =\n", a @ b)
