import cmath

y = []
x = [20.5, 21.35, 21.25, 14.75, 20.75]
for i in range(len(x)):
    a = (x[i] - 19.72) ** 2
    y.append(a)
print(y)
z = cmath.sqrt((sum(y, y[0]) / 4))
print(z * 2.13)
