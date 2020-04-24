# nhân với vector
import numpy as np

a_1 = [[1, 2, 3], [4, 5, 6]]
b_1 = [1, 2, 3]
a = np.array(a_1)
b = np.array(b_1)
print("a =\n", a)
print("b =\n", b)
print("a*b = \n", a @ b)
